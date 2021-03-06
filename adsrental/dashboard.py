from urllib.parse import urlencode
import datetime
import typing

from dateutil.relativedelta import relativedelta
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from adsrental.models import LeadAccount, Lead


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for app.
    """

    def init_with_context(self, context: typing.Dict) -> None:
        # append a link list module for "quick links"
        request = context['request']
        now = timezone.localtime(timezone.now())
        current_week_start = now - datetime.timedelta(days=now.weekday())
        prev_week_end = current_week_start - datetime.timedelta(days=1)
        prev_week_start = prev_week_end - datetime.timedelta(days=prev_week_end.weekday())
        current_month_start = now - datetime.timedelta(days=now.day - 1)

        if not request.user.is_superuser:
            # append an app list module for "Applications"
            self.children.append(modules.AppList(
                _('Applications'),
                exclude=('django.contrib.*',),
            ))
            return

        self.children.append(modules.LinkList(
            _('Reports'),
            # layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Master Report for Facebook Accounts'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxyleadaccount_changelist'),
                    urlencode(dict(
                        account_type__exact=LeadAccount.ACCOUNT_TYPE_FACEBOOK,
                        status=LeadAccount.STATUS_ACTIVE,
                        # lead__company__exact=Lead.COMPANY_FBM,
                    )),
                )],
                [_('Master Report for Amazon Accounts'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxyleadaccount_changelist'),
                    urlencode(dict(
                        account_type__exact=LeadAccount.ACCOUNT_TYPE_AMAZON,
                        status=LeadAccount.STATUS_ACTIVE,
                    )),
                )],
                [_('Master Report for ACM Google Accounts'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxyleadaccount_changelist'),
                    urlencode(dict(
                        account_type__exact=LeadAccount.ACCOUNT_TYPE_GOOGLE,
                        status=LeadAccount.STATUS_ACTIVE,
                        lead__company__exact=Lead.COMPANY_ACM,
                    )),
                )],
                [_('Facebook Screenshot in Needs Approval status'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxyleadaccount_changelist'),
                    urlencode(dict(
                        account_type__exact=LeadAccount.ACCOUNT_TYPE_FACEBOOK_SCREENSHOT,
                        status=LeadAccount.STATUS_NEEDS_APPROVAL,
                        online='online',
                    )),
                )],
                [_('Google accounts in Needs Approval status'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxyleadaccount_changelist'),
                    urlencode(dict(
                        account_type__exact=LeadAccount.ACCOUNT_TYPE_GOOGLE,
                        status=LeadAccount.STATUS_NEEDS_APPROVAL,
                        online='online',
                    )),
                )],
                [_('Check Report for current month'), '{}?{}'.format(
                    reverse('admin:adsrental_leadhistorymonth_changelist'),
                    urlencode(dict(
                        date=datetime.date.today().replace(day=1).strftime(settings.SYSTEM_DATE_FORMAT),
                        move_to_next_month__exact=0,
                    )),
                )],
                [_('Check Report for previous month'), '{}?{}'.format(
                    reverse('admin:adsrental_leadhistorymonth_changelist'),
                    urlencode(dict(
                        date=(datetime.date.today() - relativedelta(months=1)).replace(day=1).strftime(settings.SYSTEM_DATE_FORMAT),
                        move_to_next_month__exact=0,
                    )),
                )],
                [_('Devices shipped this week ({} - {})'.format(
                    current_week_start.strftime(settings.HUMAN_DATE_FORMAT),
                    now.strftime(settings.HUMAN_DATE_FORMAT),
                )), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxylead_changelist'),
                    urlencode(dict(
                        shipped_date='current_week',
                    )),
                )],
                [_('Devices shipped previous week ({} - {})'.format(
                    prev_week_start.strftime(settings.HUMAN_DATE_FORMAT),
                    prev_week_end.strftime(settings.HUMAN_DATE_FORMAT),
                )), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxylead_changelist'),
                    urlencode(dict(
                        shipped_date='previous_week',
                    )),
                )],
                [_('Devices shipped this month ({} - {})'.format(
                    current_month_start.strftime(settings.HUMAN_DATE_FORMAT),
                    now.strftime(settings.HUMAN_DATE_FORMAT),
                )), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxylead_changelist'),
                    urlencode(dict(
                        shipped_date='current_month',
                    )),
                )],
                [_('Charge back leads'), '{}?{}'.format(
                    reverse('admin:adsrental_reportproxylead_changelist'),
                    urlencode(dict(
                        lead_account__charge_back__exact='1',
                        lead_account__charge_back_billed__exact='0',
                    )),
                )],
                [_('Bundler payments report preview'), '{}'.format(
                    reverse('bundler_payments'),
                )],
                [_('Banned lead accounts last 30 days'), '{}?{}'.format(
                    reverse('admin:adsrental_leadaccount_changelist'),
                    urlencode(dict(
                        banned_date='last_30_days',
                    )),
                )],
                [_('Bundler bonuses'), '{}'.format(
                    reverse('admin_helpers:bundler_bonuses'),
                )],
                [_('Bundler daily bonuses'), '{}'.format(
                    reverse('admin_helpers:bundler_daily_bonuses'),
                )],
                [_('Lead Accounts Weekly Report preview'), '{}'.format(
                    reverse('report:lead_accounts_weekly'),
                )],
                [_('Auto Ban Soon report'), '{}'.format(
                    reverse('report:auto_ban'),
                )],
                [_('Bundler payments total report'), '{}'.format(
                    reverse('report:bundler_payments'),
                )],
                [_('Ban reason report'), '{}'.format(
                    reverse('report:ban_reason'),
                )],
                [_('DEBUG: Tunnel down'), '{}?{}'.format(
                    reverse('admin:adsrental_ec2instance_changelist'),
                    urlencode(dict(
                        lead_status='Active',
                        online='online',
                        tunnel_up='no',
                        version='latest',
                    )),
                )],
            ]
        ))
        self.children.append(modules.LinkList(
            _('Documentation'),
            # layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Admin Documentation'), '/admin/doc/', ],
                [_('FAQ: Lead documentation'), '/admin/doc/models/adsrental.lead/', ],
                [_('FAQ: RaspberryPi documentation'), '/admin/doc/models/adsrental.raspberrypi/', ],
                [_('FAQ: EC2 Instance documentation'), '/admin/doc/models/adsrental.ec2instance/', ],
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for app.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args: str, **kwargs: str) -> None:
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    # def init_with_context(self, context):
    #     """
    #     Use this method if you need to access the request context.
    #     """
    #     return super(CustomAppIndexDashboard, self).init_with_context(context)
