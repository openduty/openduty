__author__ = 'deathowl'

from datetime import datetime, timedelta
from django.db import transaction
from notification.tasks import send_notifications
from openduty.escalation_helper import get_escalation_for_service
from openduty.models import Incident
from django.utils import timezone
from notification.models import ScheduledNotification
from django.conf import settings


class NotificationHelper(object):
    @staticmethod
    def notify_incident(incident):
        notifications = NotificationHelper.generate_notifications_for_incident(incident)

        for notification in notifications:
            notification.save()
            send_notifications.apply_async((notification.id,) ,eta=notification.send_at)
    @staticmethod
    def notify_user_about_incident(incident, user, delay=None, preparedmsg = None):
        notifications = NotificationHelper.generate_notifications_for_user(incident, user, delay, preparedmsg)

        for notification in notifications:
            notification.save()
            send_notifications.apply_async((notification.id,) ,eta=notification.send_at)

    @staticmethod
    def generate_notifications_for_incident(incident):
        now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        duty_officers = []
        # if incident has been escalated, notify according to the escalated service's escalation rule
        if hasattr(incident, 'service_to_escalate_to') and incident.service_to_escalate_to is not None:
            print "escalation rule in place to " + incident.service_to_escalate_to.name
            duty_officers = get_escalation_for_service(incident.service_to_escalate_to)
            with transaction.atomic():
                incident.description = "[escalated] " + incident.description
                incident.save()
        else:
            duty_officers = get_escalation_for_service(incident.service_key)
        current_time = now

        notifications = []
        group_index = {}
        user_method_index = {}

        for officer_index, duty_officer in enumerate(duty_officers):
            if incident.event_type == Incident.RESOLVE and not duty_officer.profile.send_resolve_enabled:
                print "Skipping notification for %s because type is RESOLVE and user %s has send_resolve_enabled OFF" % (incident.incident_key, duty_officer.username)
                continue
            index = 0
            if hasattr(duty_officer ,'came_from_group' ):
                if not duty_officer.came_from_group in group_index:
                    group_index[duty_officer.came_from_group] = officer_index
                index = group_index[duty_officer.came_from_group]
            else:
                index = officer_index
            escalation_time = incident.service_key.escalate_after * (index + 1)
            escalate_at = current_time + timedelta(minutes=escalation_time)

            user_method_index[duty_officer.username] = 0
            methods = duty_officer.notification_methods.order_by('position').all()

            for method in methods:
                notification_time = incident.service_key.retry * user_method_index[duty_officer.username] + incident.service_key.escalate_after * index
                notify_at = current_time + timedelta(minutes=notification_time)
                if notify_at < escalate_at:
                    notification = ScheduledNotification()
                    notification.incident = incident
                    notification.user_to_notify = duty_officer
                    notification.notifier = method.method
                    notification.send_at = notify_at
                    uri = settings.BASE_URL + "/incidents/details/" + str(incident.id)
                    notification.message = incident.description + ". Handle at: " + uri + " Details: " + incident.details

                    notifications.append(notification)

                    print "[%s] Notify %s about %s at %s with method: %s" % (notification.incident.event_type, duty_officer.username, notification.incident.incident_key, notify_at, notification.notifier)
                else:
                    break
                user_method_index[duty_officer.username] += 1

            # todo: error handling

        return notifications

    @staticmethod
    def generate_notifications_for_user(incident, user, delay=None, preparedmsg = None):

        now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        current_time = now
        notifications = []
        methods = user.notification_methods.order_by('position').all()
        method_index = 0

        for method in methods:
            if delay is None:
                notification_time = incident.service_key.retry * method_index + incident.service_key.escalate_after
            else:
                notification_time = method_index * delay
            notify_at = current_time + timedelta(minutes=notification_time)
            notification = ScheduledNotification()
            notification.incident = incident
            notification.user_to_notify = user
            notification.notifier = method.method
            notification.send_at = notify_at
            if preparedmsg is None:
                uri = settings.BASE_URL + "/incidents/details/" + str(incident.id)
                notification.message = "A Service is experiencing a problem: " + incident.incident_key + " " + incident.description + ". Handle at: " + uri
            else:
                notification.message = preparedmsg
            notifications.append(notification)
            if notification.incident:
                print "[%s] Notify %s at %s with method: %s" % (notification.incident.event_type, user.username, notify_at, notification.notifier)
            method_index += 1

        # todo: error handling
        return notifications
