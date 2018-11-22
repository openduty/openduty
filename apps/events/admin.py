from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class EventLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'incident_key',
        'action',
        'service_key',
        'data',
        'occurred_at',
    )
    list_filter = ('user', 'incident_key', 'service_key', 'occurred_at')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.EventLog, EventLogAdmin)
