import pytest
from django_dynamic_fixture import G
from apps.policies.models import SchedulePolicy, SchedulePolicyRule
from apps.services.models import Service


@pytest.mark.django_db
def test_schedule_policy__str__():
    name = "My new Policy"
    schedule_policy = G(SchedulePolicy, name=name)

    assert schedule_policy.__str__() == name


@pytest.mark.django_db
def test_schedule_policy_natural_key():
    name = "My new Policy"
    schedule_policy = G(SchedulePolicy, name=name)

    assert schedule_policy.natural_key() == name


@pytest.mark.django_db
def test_schedule_policy_rule__str__():
    schedule_policy = G(SchedulePolicy)
    schedule_policy_rule = G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
    )

    assert schedule_policy_rule.__str__() == str(schedule_policy_rule.pk)


@pytest.mark.django_db
def test_schedule_policy_rule_get_rules_for_service():
    schedule_policy = G(SchedulePolicy)
    service = G(Service, policy=schedule_policy)
    schedule_policy_rule = G(
        SchedulePolicyRule,
        schedule_policy=schedule_policy,
    )

    assert schedule_policy_rule in schedule_policy_rule.get_rules_for_service(service)
