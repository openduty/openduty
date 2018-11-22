from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class IncidentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'service_key',
        'incident_key',
        'event_type',
        'description',
        'details',
        'occurred_at',
        'service_to_escalate_to',
    )
    list_filter = ('service_key', 'occurred_at', 'service_to_escalate_to')


class IncidentSilencedAdmin(admin.ModelAdmin):

    list_display = ('id', 'incident', 'silenced', 'silenced_until')
    list_filter = ('incident', 'silenced', 'silenced_until')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Incident, IncidentAdmin)
_register(models.IncidentSilenced, IncidentSilencedAdmin)
