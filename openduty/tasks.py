from __future__ import absolute_import
from notification.helper import NotificationHelper
from celery import shared_task
from openduty.models import Incident, IncidentSilenced, Service, ServiceSilenced

__author__ = 'deathowl'


@shared_task
def unsilence_incident(incident_id):
    incident = Incident.objects.get(id=incident_id)
    if incident.event_type == Incident.ACKNOWLEDGE:
        incident.event_type = Incident.TRIGGER
        incident.save()
        NotificationHelper.notify_incident(incident)
    silenced_incident = IncidentSilenced.objects.filter(incident=incident)
    silenced_incident.delete()


@shared_task
def unsilence_service(service_id):
    service = Service.objects.get(id=service_id)
    silenced_service = ServiceSilenced.objects.filter(service=service)
    silenced_service.delete()
