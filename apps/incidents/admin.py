from django.contrib import admin
from apps.incidents.models import Incident, IncidentSilenced


@admin.register(Incident)
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


@admin.register(IncidentSilenced)
class IncidentSilencedAdmin(admin.ModelAdmin):
    list_display = ('id', 'incident', 'silenced', 'silenced_until')
    list_filter = ('incident', 'silenced', 'silenced_until')
