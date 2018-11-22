__author__ = 'catalincoroeanu'

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group
from schedule.models import Calendar
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class SchedulePolicy(models.Model):
    """
    Schedule policy
    """
    name = models.CharField(max_length=80, unique=True)
    repeat_times = models.IntegerField()

    class Meta:
        verbose_name = _('schedule_policy')
        verbose_name_plural = _('schedule_policies')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)


@python_2_unicode_compatible
class SchedulePolicyRule(models.Model):
    """
    Schedule rule
    """
    schedule_policy = models.ForeignKey(SchedulePolicy, related_name='rules', on_delete=models.CASCADE)
    position = models.IntegerField()
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Calendar, blank=True, null=True, on_delete=models.CASCADE)
    escalate_after = models.IntegerField()

    class Meta:
        verbose_name = _('schedule_policy_rule')
        verbose_name_plural = _('schedule_policy_rules')

    def __str__(self):
        return str(self.id)

    @classmethod
    def getRulesForService(cls, service):
        return cls.objects.filter(schedule_policy=service.policy.id)
