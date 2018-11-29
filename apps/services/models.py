import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from apps.accounts.models import Token
from apps.policies.models import SchedulePolicy


@python_2_unicode_compatible
class Service(models.Model):
    """
    Incidents are representations of a malfunction in the system.
    """
    name = models.CharField(max_length=80, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    retry = models.IntegerField(blank=True, null=True)
    policy = models.ForeignKey(SchedulePolicy, blank=True, null=True, on_delete=models.CASCADE)
    escalate_after = models.IntegerField(blank=True, null=True)
    notifications_disabled = models.BooleanField(default=False)
    send_resolve_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('service')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.id)


@python_2_unicode_compatible
class ServiceTokens(models.Model):
    """
    Service tokens
    """
    name = models.CharField(max_length=80)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    token_id = models.ForeignKey(Token, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('service_tokens')
        verbose_name_plural = _('service_tokens')

    def __str__(self):
        return self.name


class ServiceSilenced(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    silenced = models.BooleanField(default=False)
    silenced_until = models.DateTimeField()
