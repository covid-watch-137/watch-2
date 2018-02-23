from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.db.models import Count

from adsrental.models.bundler import Bundler
from adsrental.models.lead import Lead


class BundlerAdmin(admin.ModelAdmin):
    model = Bundler
    list_display = ('id', 'name', 'utm_source', 'adsdb_id', 'email', 'phone', 'leads_count', )
    actions = (
        'assign_leads_for_this_bundler',
    )

    def get_queryset(self, request):
        qs = super(BundlerAdmin, self).get_queryset(request)
        return qs.annotate(leads_count=Count('lead'))

    def assign_leads_for_this_bundler(self, request, queryset):
        for bundler in queryset:
            leads = Lead.objects.filter(utm_source=bundler.utm_source)
            if leads:
                leads.update(bundler=bundler)
                messages.success(request, 'Bundler {} is assigned to {} leads.'.format(
                    bundler, leads.count(),
                ))
            else:
                messages.success(request, 'Bundler {} has no leads.'.format(
                    bundler, leads.count(),
                ))
            leads = Lead.objects.filter(bundler=bundler).exclude(utm_source=bundler.utm_source)
            if leads:
                leads.update(bundler=None)
                messages.success(request, 'Bundler {} is unassigned from {} leads.'.format(
                    bundler, leads.count(),
                ))

    def leads_count(self, inst):
        return inst.leads_count
