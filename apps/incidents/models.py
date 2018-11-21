__author__ = 'catalincoroeanu'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
from django.conf import settings
from apps.services.models import Service


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class Incident(models.Model):
    TRIGGER = "trigger"
    RESOLVE = "resolve"
    ACKNOWLEDGE = "acknowledge"
    UNACKNOWLEDGE = "unacknowledge"
    ESCALATE = "escalate"
    """
    Incidents are representations of a malfunction in the system.
    """
    service_key = models.ForeignKey(Service,related_name="incident", on_delete=models.CASCADE)
    incident_key = models.CharField(max_length=200)
    event_type = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    details = models.TextField()
    occurred_at = models.DateTimeField()
    service_to_escalate_to = models.ForeignKey(
        Service,related_name="service_to_escalate_to_id",
        null=True, blank=True, default=None, on_delete=models.CASCADE)

    @property
    def color(self):
        colort_dict = {'acknowledge': 'warning',
                       'unacknowledge': 'warning',
                       'resolve': 'success',
                       'silence_service': 'active',
                       'silence_incident': 'active',
                       'forward': 'info',
                       'trigger': 'trigger',
                       'log': ''}
        return colort_dict[self.event_type]

    class Meta:
        verbose_name = _('incidents')
        verbose_name_plural = _('incidents')
        unique_together = (("service_key", "incident_key"),)

    def __str__(self):
        return self.incident_key

    def natural_key(self):
        return (self.service_key, self.incident_key)
    def clean(self):
        if self.event_type not in ['trigger', 'acknowledge','unacknowledge', 'resolve']:
            raise ValidationError("'%s' is an invalid event type, valid values are 'trigger', 'acknowledge', 'unacknowledge' and 'resolve'" % self.event_type)


class IncidentSilenced(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    silenced = models.BooleanField(default=False)
    silenced_until = models.DateTimeField()
