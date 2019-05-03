import pytest
from datetime import timedelta
from django.utils import timezone
from django_dynamic_fixture import G
from apps.notification.models import UserNotificationMethod, ScheduledNotification
from apps.incidents.models import Incident


@pytest.mark.django_db
def test_create_user_notification():
    user_notification = G(UserNotificationMethod)
    assert user_notification.pk
    assert user_notification.__str__() == str(user_notification.id)


@pytest.mark.django_db
def test_create_schedule_notification():
    schedule_notification = G(ScheduledNotification)
    assert schedule_notification.pk
    assert schedule_notification.__str__() == str(schedule_notification.id)


@pytest.mark.django_db
def test_schedule_notification_remove_all_for_incident():
    incident = G(Incident)
    schedule_notification = G(ScheduledNotification, incident=incident)
    assert schedule_notification.pk
    schedule_notification.remove_all_for_incident(incident)
    assert not ScheduledNotification.objects.count()


@pytest.mark.django_db
def test_schedule_notification_get_notifications_to_send():
    schedule_notification_1 = G(
        ScheduledNotification,
        send_at=timezone.now() - timedelta(hours=2)
    )
    schedule_notification_2 = G(
        ScheduledNotification,
        send_at=timezone.now() + timedelta(hours=2)
    )
    assert schedule_notification_1.pk
    assert schedule_notification_2.pk
    schedule_notification_list = schedule_notification_1.get_notifications_to_send(None)
    assert len(schedule_notification_list) == 1
    assert schedule_notification_2 not in schedule_notification_list
