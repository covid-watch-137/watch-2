import datetime
from dateutil import parser

from django.views import View
from django.utils import timezone
from django.shortcuts import Http404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from adsrental.models.lead_account import LeadAccount
from adsrental.models.bundler import Bundler


class AdminBundlerBonusesAccountsView(View):
    @method_decorator(login_required)
    def get(self, request, bundler_id, extra=False):
        if not request.user.is_superuser:
            raise Http404

        bundler = Bundler.objects.filter(id=bundler_id).first()
        if not bundler:
            raise Http404

        now = timezone.localtime(timezone.now())
        start_date_str = request.GET.get('start_date')
        if start_date_str:
            start_date = parser.parse(start_date_str).replace(tzinfo=timezone.get_current_timezone())
        else:
            start_date = now
        end_date_str = request.GET.get('end_date')
        if end_date_str:
            end_date = parser.parse(end_date_str).replace(tzinfo=timezone.get_current_timezone())
        else:
            end_date = now

        start_date = start_date.replace(hour=0, minute=0, second=0)
        end_date = end_date.replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)

        dates_list = []
        for i in range(-1, 2):
            if start_date + datetime.timedelta(days=7 * i) < now:
                dates_list.append(dict(
                    start_date=start_date + datetime.timedelta(days=7 * i),
                    end_date=end_date + datetime.timedelta(days=7 * i) - datetime.timedelta(days=1),
                ))

        lead_accounts = LeadAccount.objects.filter(
            account_type__in=LeadAccount.ACCOUNT_TYPES_FACEBOOK,
            lead__bundler=bundler,
            primary=True,
            qualified_date__gt=start_date,
            qualified_date__lt=end_date,
        ).prefetch_related('lead').order_by('qualified_date')

        extra_lead_accounts = LeadAccount.objects.filter(
            account_type__in=LeadAccount.ACCOUNT_TYPES_FACEBOOK,
            lead__bundler__bonus_receiver_bundler=bundler,
            primary=True,
            qualified_date__gt=start_date,
            qualified_date__lt=end_date,
        ).prefetch_related('lead', 'lead__bundler').order_by('qualified_date')

        return render(request, 'admin/bundler_bonuses_accounts.html', dict(
            lead_accounts=lead_accounts,
            extra_lead_accounts=extra_lead_accounts,
            bundler=bundler,
            start_date=start_date,
            end_date=end_date - datetime.timedelta(days=1),
            dates_list=dates_list,
        ))
