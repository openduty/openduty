from django.contrib import admin
from apps.events.models import EventLog


@admin.register(EventLog)
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
