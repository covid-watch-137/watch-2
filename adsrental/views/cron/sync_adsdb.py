from dateutil import parser

import requests
from django.utils import timezone
from django.conf import settings
from django.views import View
from django.http import JsonResponse

from adsrental.models import LeadAccount, User


class SyncAdsDBView(View):
    def get(self, request):
        messages = []
        accounts = []
        not_found_count = 0
        now = timezone.now()
        auth = requests.auth.HTTPBasicAuth(settings.ADSDB_USERNAME, settings.ADSDB_PASSWORD)
        for page in range(1, 1000):
            try:
                data = requests.post(
                    'https://www.adsdb.io/api/v1/accounts/get',
                    auth=auth,
                    json={
                        'limit': 200,
                        'page': 1,
                    },
                ).json()
            except requests.RequestException:
                continue
            if not data.get('success') or not data.get('data'):
                break
            for account in data['data']:
                if account['account_status'] != 'Dead':
                    continue
                try:
                    banned_date = parser.parse(account.get('dead_date'))
                except:
                    continue

                if now - banned_date < datetime.timedelta(days=4):
                    continue

                accounts.append(account)

        messages.append(f'Total accounts {len(accounts)}')
        user = User.objects.get(email='volshebnyi@gmail.com')
        for account in accounts:
            if account['account_status'] != 'Dead':
                continue
            la = LeadAccount.objects.filter(adsdb_account_id=account.get('id')).first()
            if not la:
                not_found_count += 1
                continue
            if la.status == LeadAccount.STATUS_BANNED:
                continue

            messages.append(f'{la.account_type} account {la.username} banned from {la.status}')
            reason = LeadAccount.BAN_REASON_FACEBOOK_POLICY
            if la.account_type == LeadAccount.ACCOUNT_TYPE_GOOGLE:
                reason = LeadAccount.BAN_REASON_GOOGLE_POLICY
            la.ban(edited_by=user, reason=reason)

        return JsonResponse({
            'messages': messages,
            'total_banned': len(messages) - 1,
            'not_found': not_found_count,
        })