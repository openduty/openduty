import pytest
from django.utils import timezone
import datetime
from datetime import timedelta, datetime
from django.core.exceptions import ValidationError
from django_dynamic_fixture import G
from schedule.models import Calendar, Event
from apps.services.models import Service
from apps.policies.models import SchedulePolicy, SchedulePolicyRule, Group
from apps.incidents.escalation_helper import (
    get_escalation_for_service, get_current_events_users, get_events_users_inbetween, services_where_user_is_on_call
)
from apps.incidents.models import Incident, IncidentSilenced, Service
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
def test_get_escalation_works_with_no_recurrence(base_user):
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy)
    calendar = G(Calendar)
    group = G(Group)
    base_user.groups.add(group)
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        user_id=base_user.id
    )
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        group_id=group.id
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group.name,
    )
    events = get_escalation_for_service(service)
    assert len(events) == 2


@pytest.mark.django_db
def test_get_escalation_for_service_with_notifications_disabled(base_user):
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy, notifications_disabled=True)
    calendar = G(Calendar)
    group = G(Group)
    base_user.groups.add(group)
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        user_id=base_user.id
    )
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        group_id=group.id
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group.name,
    )
    events = get_escalation_for_service(service)
    assert len(events) == 0


@pytest.mark.django_db
def test_get_escalation_for_service_no_schedule(base_user, other_user):
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy, notifications_disabled=False)
    calendar = G(Calendar)
    group = G(Group)
    other_user.groups.add(group)
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        user_id=base_user
    )
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        group_id=group
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    events = get_escalation_for_service(service)
    assert len(events) == 3


@pytest.mark.django_db
def test_get_escalation_fails_with_no_recurrence_after_event_end(base_user):
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy, )
    calendar = G(Calendar)
    group = G(Group)
    base_user.groups.add(group)
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        user_id=base_user
    )
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        group_id=group
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group.name,
    )
    events = get_escalation_for_service(service)
    assert len(events) == 2


@pytest.mark.django_db
def test_get_current_events_users(base_user):
    calendar = G(Calendar)
    event = G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    current_events_users = get_current_events_users(calendar)
    assert len(current_events_users)


@pytest.mark.django_db
def test_get_current_events_users_by_group(base_user):
    calendar = G(Calendar)
    group = G(Group)
    base_user.groups.add(group)
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group.name
    )
    current_events_users = get_current_events_users(calendar)
    assert len(current_events_users)


@pytest.mark.django_db
def test_get_events_users_inbetween_with_timezone(base_user):
    calendar = G(Calendar)
    since = timezone.now() - timedelta(days=2)
    until = timezone.now() + timedelta(days=2)
    event = G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    events_users_in_between = get_events_users_inbetween(calendar, since, until)
    assert len(events_users_in_between) == 1


@pytest.mark.django_db
def test_get_events_users_inbetween_no_timezone(base_user):
    calendar = G(Calendar)
    since = datetime.now() - timedelta(days=2)
    until = datetime.now() + timedelta(days=2)
    event = G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    events_users_in_between = get_events_users_inbetween(calendar, since, until)
    assert len(events_users_in_between) == 1


@pytest.mark.django_db
def test_get_events_users_inbetween_with_users(base_user):
    Group.objects.all().delete()
    calendar = G(Calendar)
    since = datetime.now() - timedelta(days=2)
    until = datetime.now() + timedelta(days=2)
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=base_user.username,
    )
    events_users_in_between = get_events_users_inbetween(calendar, since, until)
    assert len(events_users_in_between) == 1


@pytest.mark.django_db
def test_get_events_users_inbetween_with_group(base_user):
    Group.objects.all().delete()
    calendar = G(Calendar)
    group = G(Group)
    group2 = G(Group)
    base_user.groups.add(group, group2)
    since = datetime.now() - timedelta(days=2)
    until = datetime.now() + timedelta(days=2)
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group.name,
    )
    G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=base_user,
        title=group2.name,
    )
    events_users_in_between = get_events_users_inbetween(calendar, since, until)
    assert len(events_users_in_between) == 1

@pytest.mark.django_db
def test_services_where_user_is_on_call(base_user, other_user):
    schedule_policy = G(SchedulePolicy)
    calendar = G(Calendar)
    calendar2 = G(Calendar)
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar2,
        escalate_after=1,
        user_id=base_user,
        group_id=None
    )
    event = G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar,
        creator=other_user,
        title=other_user.username,
    )
    G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
        user_id=None,
        group_id=None
    )
    service = G(Service, policy=schedule_policy, notifications_disabled=False)

    assert service in services_where_user_is_on_call(other_user)
    assert service in services_where_user_is_on_call(base_user)
