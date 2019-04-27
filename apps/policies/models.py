from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import Group
from schedule.models import Calendar


class SchedulePolicy(models.Model):
    """
    Schedule policy
    """
    name = models.CharField(max_length=80, unique=True)
    repeat_times = models.IntegerField()

    class Meta:
        verbose_name = _('Schedule policy')
        verbose_name_plural = _('Schedule policies')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class SchedulePolicyRule(models.Model):
    """
    Schedule rule
    """
    schedule_policy = models.ForeignKey('SchedulePolicy', related_name='rules', on_delete=models.CASCADE)
    position = models.IntegerField()
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='rules')
    group_id = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, related_name='rules')
    schedule = models.ForeignKey(Calendar, blank=True, null=True, on_delete=models.CASCADE, related_name='rules')
    escalate_after = models.IntegerField()

    class Meta:
        verbose_name = _('schedule_policy_rule')
        verbose_name_plural = _('schedule_policy_rules')

    def __str__(self):
        return f"{self.id}"

    @classmethod
    def get_rules_for_service(cls, service):
        return cls.objects.filter(schedule_policy=service.policy.id)
