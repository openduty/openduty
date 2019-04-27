import pytest
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import Group
from rest_framework import status
from schedule.models import Calendar
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user
from apps.policies.views import (
    SchedulePolicyCreateView, SchedulePolicyCreateOrUpdateMixin
)
from apps.policies.models import SchedulePolicy


@pytest.mark.django_db
def test_schedule_policy_create(authenticated_client):
    c = authenticated_client
    policy_name = "My New Policy"
    repeat_times = 3
    response = c.post(
        reverse('SchedulePolicyCreateView'),
        data={"name": policy_name, "repeat_times": repeat_times}
    )
    assert response.status_code == status.HTTP_302_FOUND
    assert SchedulePolicy.objects.count() == 1


@pytest.mark.django_db
def test_schedule_policy_get_create_view(base_user):
    request = RequestFactory().get(reverse('SchedulePolicyCreateView'))
    request.user = base_user
    response = SchedulePolicyCreateView.as_view()(request)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_schedule_policy_get_update_view(authenticated_client):
    c = authenticated_client
    policy = G(SchedulePolicy)
    response = c.get(reverse('SchedulePolicyUpdateView', args=[policy.id]))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_extra_context(base_user):
    user = base_user
    G(Calendar)
    G(Group)
    policy = G(SchedulePolicy)
    mixin = SchedulePolicyCreateOrUpdateMixin()
    assert mixin.get_extra_context(policy)
    assert not mixin.get_extra_context(None)


@pytest.mark.django_db
def test_after_form_valid(base_user):
    user = base_user
    calendar = G(Calendar)
    group = G(Group)
    policy = G(SchedulePolicy)
    mixin = SchedulePolicyCreateOrUpdateMixin()
    escalate_list = [ f'user|{user.id}', f'group|{group.id}', f'calendar|{calendar.id}']
    mixin.after_form_valid(escalate_list, policy, '/')
    assert policy.rules.count()


