from __future__ import unicode_literals

from django.db import models


class Bundler(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    utm_source = models.CharField(max_length=50, db_index=True, null=True, blank=True)
    adsdb_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bank_info = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def get_by_utm_source(cls, utm_source):
        utm_source_digits = ''.join([i for i in utm_source if i.isdigit()])
        if not utm_source_digits:
            return None
        return cls.objects.filter(utm_source=int(utm_source_digits)).first()

    def __str__(self):
        return '{} ({})'.format(self.name, self.utm_source)