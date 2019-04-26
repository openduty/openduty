from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from schedule.models import Calendar, Event
from schedule.periods import Year
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user
from apps.schedules.views import SchedulesDetailView
import pytest


@pytest.mark.django_db
def test_schedule_detail_view_works_with_query_args(authenticated_client):
    c = authenticated_client
    calendar = G(Calendar)
    response = c.get(
        reverse('calendar_details', args=[calendar.slug]),
        {'month': '11', 'year': '2014'},
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_on_call_users(authenticated_client, other_user, base_user):
    c = authenticated_client
    calendar = G(Calendar)
    G(
        Event,
        title=other_user.username,
        calendar=calendar,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        creator=other_user
    )
    G(
        Event,
        title=base_user.username,
        calendar=calendar,
        start=timezone.now() - timedelta(days=1),
        end=timezone.now() + timedelta(days=1),
        creator=base_user
    )
    response = c.get(
        reverse('calendar_details', args=[calendar.slug]),
        {'month': str(timezone.now().month), 'year': str(timezone.now().year)},
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_schedule_detail_incorrect_date_format(authenticated_client):
    c = authenticated_client
    calendar = G(Calendar)
    kwargs = {
         'month': str(timezone.now().month + 12),
         'year': str((timezone.now() + timedelta(days=1000)).year)
     }
    response = c.get(
        reverse('calendar_details', args=[calendar.slug]), kwargs,
    )
    assert response.status_code == 404

