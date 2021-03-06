from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from apps.incidents.models import Incident


class UserNotificationMethod(models.Model):
    """
    Schedule rule
    """

    METHOD_TWILIO_SMS = 'twilio_sms'
    METHOD_TWILIO_CALL = 'twilio_call'
    METHOD_EMAIL = 'email'
    METHOD_PUSHOVER = 'pushover'
    METHOD_XMPP = 'xmpp'
    METHOD_SLACK = 'slack'
    METHOD_PROWL = 'prowl'
    METHOD_ROCKET = 'rocket'
    METHOD_HIPCHAT = 'hipchat'


    methods = [METHOD_XMPP, METHOD_PUSHOVER, METHOD_EMAIL, METHOD_TWILIO_SMS, METHOD_TWILIO_CALL, METHOD_SLACK, METHOD_PROWL, METHOD_ROCKET, METHOD_HIPCHAT]

    user = models.ForeignKey(User, related_name='notification_methods', on_delete=models.CASCADE)
    position = models.IntegerField()
    method = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('user_notification_method')
        verbose_name_plural = _('user_notification_methods')
        db_table = 'openduty_usernotificationmethod'

    def __str__(self):
        return str(self.id)


class ScheduledNotification(models.Model):
    notifier = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    user_to_notify = models.ForeignKey(User, on_delete=models.CASCADE)
    send_at = models.DateTimeField()
    incident = models.ForeignKey(Incident, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('scheduled_notifications')
        verbose_name_plural = _('scheduled_notifications')
        db_table = 'openduty_schedulednotification'

    def __str__(self):
        return str(self.id)

    @staticmethod
    def remove_all_for_incident(incident):
        notices = ScheduledNotification.objects.filter(incident=incident)
        for notice in notices:
            notice.delete()

    @staticmethod
    def get_notifications_to_send(date=None):
        if not date:
            date = timezone.now()
        return ScheduledNotification.objects.filter(send_at__lte=date)
