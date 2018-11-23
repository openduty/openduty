from __future__ import absolute_import

from celery import shared_task
from apps.notification.notifier.pushover import PushoverNotifier
# from notification.notifier.xmpp import XmppNotifier
from apps.notification.notifier.email import EmailNotifier
from apps.notification.notifier.twilio_sms import TwilioSmsNotifier
from apps.notification.notifier.twilio_call import TwilioCallNotifier
from apps.notification.notifier.slack import SlackNotifier
from apps.notification.notifier.prowl import ProwlNotifier
from apps.notification.notifier.rocket import RocketNotifier
from apps.notification.notifier.hipchat import HipchatNotifier
from apps.notification.models import ScheduledNotification, UserNotificationMethod
from django.conf import settings
from django.utils import timezone

from apps.events.models import EventLog


@shared_task
def send_notifications(notification_id):
    try:
        notification = ScheduledNotification.objects.get(id = notification_id)
        # if notification.notifier == UserNotificationMethod.METHOD_XMPP:
        #     notifier = XmppNotifier(settings.XMPP_SETTINGS)
        if notification.notifier == UserNotificationMethod.METHOD_EMAIL:
            notifier = EmailNotifier(settings.EMAIL_SETTINGS)
        if notification.notifier == UserNotificationMethod.METHOD_TWILIO_SMS:
            notifier = TwilioSmsNotifier(settings.TWILIO_SETTINGS)
        if notification.notifier == UserNotificationMethod.METHOD_TWILIO_CALL:
            notifier = TwilioCallNotifier(settings.TWILIO_SETTINGS)
        if notification.notifier == UserNotificationMethod.METHOD_SLACK:
            notifier = SlackNotifier(settings.SLACK_SETTINGS)
        elif notification.notifier == UserNotificationMethod.METHOD_PUSHOVER:
            notifier = PushoverNotifier()
        elif notification.notifier == UserNotificationMethod.METHOD_PROWL:
            notifier = ProwlNotifier(settings.PROWL_SETTINGS)
        elif notification.notifier == UserNotificationMethod.METHOD_ROCKET:
            notifier = RocketNotifier()
        elif notification.notifier == UserNotificationMethod.METHOD_HIPCHAT:
            notifier = HipchatNotifier(settings.HIPCHAT_SETTINGS)

        notifier.notify(notification)
        # Log successful notification
        logmessage = EventLog()
        if notification.incident:
            logmessage.service_key = notification.incident.service_key
            logmessage.incident_key = notification.incident
            logmessage.user = notification.user_to_notify
            logmessage.action = 'notified'
            logmessage.data = "Notification sent to %s about %s service via %s" % (notification.user_to_notify, logmessage.service_key, notification.notifier, )
            logmessage.occurred_at = timezone.now()
            logmessage.save()
            return (logmessage.data)
        if notification.notifier != UserNotificationMethod.METHOD_TWILIO_CALL:
            # In case of a twilio call, we need the object for TWiml generation
            notification.delete()
    except ScheduledNotification.DoesNotExist:
        pass #Incident was resolved. NOP.
    except Exception as e:
                # Log successful notification
        logmessage = EventLog()
        if notification.incident:
            logmessage.service_key = notification.incident.service_key
            logmessage.incident_key = notification.incident
            logmessage.user = notification.user_to_notify
            logmessage.action = 'notification_failed'
            logmessage.data = "Sending notification failed to %s about %s service because %s" % (notification.user_to_notify, logmessage.service_key, e,)
            logmessage.occurred_at = timezone.now()
            logmessage.save()
            return (logmessage.data)
        raise
