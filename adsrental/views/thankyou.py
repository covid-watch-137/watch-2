import typing

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from adsrental.models.lead import Lead


class ThankyouView(View):
    '''
    page where use can provide his *splashtop_id*. Populates *splashtop_id* in :model:`adsrental.Lead`.
    '''
    def get(self, request: HttpRequest, leadid: typing.Optional[str] = None) -> HttpResponse:
        lead = Lead.objects.filter(leadid=leadid).first()
        return render(request, 'thankyou.html', dict(
            email=lead and lead.email,
        ))

    def post(self, request: HttpRequest, leadid: typing.Optional[str] = None) -> HttpResponse:
        lead = Lead.objects.filter(leadid=leadid).first()
        if lead:
            lead.splashtop_id = request.POST.get('splashtop_id')
            lead.save()
        return redirect('thankyou')


class ThankyouScreenshotView(View):
    '''
    Page with instructions for screenshot FB accounts.
    '''
    def get(self, request: HttpRequest, leadid: typing.Optional[str] = None) -> HttpResponse:
        return render(request, 'thankyou_screenshot.html', dict())
