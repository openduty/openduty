import pytest
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django_dynamic_fixture import G
from schedule.models import Calendar, Event, Rule
from apps.services.models import Service
from apps.policies.models import SchedulePolicy, SchedulePolicyRule
from apps.incidents.escalation_helper import get_escalation_for_service
from apps.incidents.models import Incident, IncidentSilenced, Service


@pytest.mark.skip
@pytest.mark.django_db
def test_get_escalation_works_with_no_recurrence():
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy)
    calendar = G(Calendar)
    schedule_policy_rule = G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
        position=0,
        schedule=calendar,
        escalate_after=1,
    )
    event = G(
        Event,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        calendar=calendar
    )
    events = get_escalation_for_service(service)
    assert len(events) == 2
