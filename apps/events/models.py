__author__ = 'catalincoroeanu'

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from apps.services.models import Service


@python_2_unicode_compatible
class EventLog(models.Model):
    """
    Event Log
    """
    ACTIONS = (('acknowledge', 'acknowledge'),
               ('unacknowledge', 'unacknowledge'),
               ('resolve', 'resolve'),
               ('silence_service', 'silence service'),
               ('unsilence_service', 'unsilence service'),
               ('silence_incident', 'silence incident'),
               ('unsilence_incident', 'unsilence incident'),
               ('forward', 'forward'),
               ('log', 'log'),
               ('notified','notified'),
               ('notification_failed', 'notification failed'),
               ('trigger', 'trigger'))

    @property
    def color(self):
        colort_dict = {
            'acknowledge': 'warning',
            'unacknowledge' : 'warning',
            'resolve': 'success',
            'silence_service': 'active',
            'unsilence_service': 'active',
            'silence_incident': 'active',
            'unsilence_incident': 'active',
            'forward': 'info',
            'escalate': 'info',
            'trigger': 'trigger',
            'notified': 'success',
            'notification_failed': 'danger',
            'log': ''
        }
        return colort_dict[self.action]

    user = models.ForeignKey(User, blank=True, default=None, null=True, related_name='users', on_delete=models.CASCADE)
    incident_key = models.ForeignKey('Incident', blank=True, null=True, on_delete=models.CASCADE)
    action = models.CharField(choices=ACTIONS, default='log', max_length=100)
    service_key = models.ForeignKey(Service, on_delete=models.CASCADE)
    data = models.TextField()
    occurred_at = models.DateTimeField()

    class Meta:
        verbose_name = _('eventlog')
        verbose_name_plural = _('eventlog')

    def __str__(self):
        return self.data

    def natural_key(self):
        return self.service_key, self.id
