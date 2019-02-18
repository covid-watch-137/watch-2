import datetime
import io
import decimal

from django.db.models import Q, Sum
from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.files.base import ContentFile
from django.contrib import messages
from xhtml2pdf import pisa

from adsrental.models.lead_account import LeadAccount
from adsrental.models.bundler import Bundler
from adsrental.models.bundler_payment import BundlerPayment
from adsrental.models.bundler_payments_report import BundlerPaymentsReport


class BundlerPaymentsView(View):
    @method_decorator(login_required)
    def get(self, request, bundler_id, report_id):
        bundlers = Bundler.objects.all()

        if bundler_id is not None:
            bundlers = bundlers.filter(id=bundler_id)

        available_bundlers = []
        for bundler in bundlers:
            if request.user.can_access_bundler(bundler):
                available_bundlers.append(bundler)

        if not available_bundlers:
            raise Http404

        now = timezone.localtime(timezone.now())
        today = now.replace(hour=0, minute=0, second=0)
        yesterday = (timezone.localtime(timezone.now()) - datetime.timedelta(days=1)).date()
        report_date = yesterday

        if report_id is not None:
            report = get_object_or_404(BundlerPaymentsReport, id=report_id)
            report_date = report.date

        bundler_payments = BundlerPayment.objects.filter(
            ready=True,
            report_id=report_id,
            bundler__in=available_bundlers,
            datetime__lte=today,
        ).exclude(
            payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_CHARGEBACK,
        ).select_related(
            'bundler',
            'lead_account',
            'lead_account__lead',
            'lead_account__lead__bundler',
        ).order_by('-payment')

        bundler_chargebacks = BundlerPayment.objects.filter(
            ready=True,
            report_id=report_id,
            bundler__in=available_bundlers,
            datetime__lte=today,
            payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_CHARGEBACK,
        ).select_related(
            'bundler',
            'lead_account',
            'lead_account__lead',
        ).order_by('-payment')
        bundler_payments_total_by_bundler = bundler_payments.values('bundler_id', 'bundler__name', 'bundler__utm_source').annotate(
            payment__sum=Sum('payment'),
            own_payment_facebook__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_MAIN, lead_account__account_type__in=LeadAccount.ACCOUNT_TYPES_FACEBOOK)),
            own_payment_google__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_MAIN, lead_account__account_type=LeadAccount.ACCOUNT_TYPE_GOOGLE)),
            own_payment_amazon__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_MAIN, lead_account__account_type=LeadAccount.ACCOUNT_TYPE_AMAZON)),
            own_payment__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_MAIN)),
            children_payment_facebook__sum=Sum('payment', filter=Q(payment_type__in=BundlerPayment.PAYMENT_TYPES_PARENT, lead_account__account_type__in=LeadAccount.ACCOUNT_TYPES_FACEBOOK)),
            children_payment_google__sum=Sum('payment', filter=Q(payment_type__in=BundlerPayment.PAYMENT_TYPES_PARENT, lead_account__account_type=LeadAccount.ACCOUNT_TYPE_GOOGLE)),
            children_payment_amazon__sum=Sum('payment', filter=Q(payment_type__in=BundlerPayment.PAYMENT_TYPES_PARENT, lead_account__account_type=LeadAccount.ACCOUNT_TYPE_AMAZON)),
            children_payment__sum=Sum('payment', filter=Q(payment_type__in=BundlerPayment.PAYMENT_TYPES_PARENT)),
            payment_bonus__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_BONUS)),
            payment_sum=Sum('payment'),
        ).order_by('-payment__sum')
        bundler_payments_total = bundler_payments.aggregate(
            payment_facebook__sum=Sum('payment', filter=Q(lead_account__account_type__in=LeadAccount.ACCOUNT_TYPES_FACEBOOK)),
            payment_google__sum=Sum('payment', filter=Q(lead_account__account_type=LeadAccount.ACCOUNT_TYPE_GOOGLE)),
            payment_amazon__sum=Sum('payment', filter=Q(lead_account__account_type=LeadAccount.ACCOUNT_TYPE_AMAZON)),
            payment_bonus__sum=Sum('payment', filter=Q(payment_type=BundlerPayment.PAYMENT_TYPE_BONUS)),
            payment__sum=Sum('payment'),
        )
        bundler_payments_by_bundler_id = {}
        children_bundler_payments_by_bundler_id = {}
        bonus_bundler_payments_by_bundler_id = {}
        for record in bundler_payments_total_by_bundler:
            record_bundler_id = record['bundler_id']
            bundler_payments_for_id = bundler_payments.filter(bundler_id=record_bundler_id)
            bundler_payments_by_bundler_id[record_bundler_id] = bundler_payments_for_id.filter(payment_type=BundlerPayment.PAYMENT_TYPE_ACCOUNT_MAIN).order_by('lead_account__account_type')
            children_bundler_payments_by_bundler_id[record_bundler_id] = bundler_payments_for_id.filter(payment_type__in=BundlerPayment.PAYMENT_TYPES_PARENT).order_by('lead_account__account_type', 'lead_account__lead__bundler')
            bonus_bundler_payments_by_bundler_id[record_bundler_id] = bundler_payments_for_id.filter(payment_type=BundlerPayment.PAYMENT_TYPE_BONUS).order_by('datetime')

        bundler_chargebacks_by_bundler_id = {}
        for record in bundler_payments_total_by_bundler:
            record_bundler_id = record['bundler_id']
            chargebacks = bundler_chargebacks.filter(bundler_id=record_bundler_id)
            bundler_chargebacks_by_bundler_id[record_bundler_id] = []
            for chargeback in chargebacks:
                if record['payment__sum'] + chargeback.payment >= 0:
                    chargebacks.append(chargeback)
                    record['payment__sum'] = record['payment__sum'] + chargeback.payment
                    bundler_payments_total['payment__sum'] = bundler_payments_total['payment__sum'] + chargeback.payment
                    bundler_payments_total['chargeback__sum'] = bundler_payments_total.get('chargeback__sum', decimal.Decimal('0.00')) - chargeback.payment

        context = dict(
            bundler_id=bundler_id,
            report_id=report_id,
            user=request.user,
            end_date=report_date,
            payments=bundler_payments,
            payments_total_by_bundler=bundler_payments_total_by_bundler,
            payments_total=bundler_payments_total,
            payments_by_bundler_id=bundler_payments_by_bundler_id,
            bonus_payments_by_bundler_id=bonus_bundler_payments_by_bundler_id,
            chargebacks_by_bundler_id=bundler_chargebacks_by_bundler_id,
            children_payments_by_bundler_id=children_bundler_payments_by_bundler_id,
            show_bundler_name=request.user.is_superuser or request.user.is_bookkeeper(),
            allow_change=request.user.is_superuser or request.user.is_bookkeeper(),
            show_summary=request.user.is_superuser or request.user.is_bookkeeper(),
        )

        if request.GET.get('save'):
            html = render_to_string(
                'bundler_payments_pdf.html',
                dict(**context, pdf=True),
                request=request,
            )
            pdf_stream = io.BytesIO()
            pisa.pisaDocument(io.BytesIO(html.encode('UTF-8')), dest=pdf_stream)
            pdf_stream.seek(0)

            report = BundlerPaymentsReport(
                date=today,
                html=html,
                pdf=ContentFile(pdf_stream.read(), name='{}.pdf'.format(yesterday)),
            )
            report.save()
            bundler_payments.update(report=report, paid=True)
            for chargebacks in bundler_chargebacks_by_bundler_id.values():
                for chargeback in chargebacks:
                    chargeback.report = report
                    chargeback.paid = True
                    chargeback.save()

            messages.success(request, 'New report was successfully generated')
            if request.user.is_bookkeeper():
                return redirect('bookkeeper_reports_list')
            return redirect('admin:adsrental_bundlerpaymentsreport_changelist')

        return render(request, 'bundler_payments.html', context)
