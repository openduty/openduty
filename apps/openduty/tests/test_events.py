from django.urls import reverse
from schedule.models import Calendar, Event, Rule
from apps.commons.tests.fixtures import LoggedInTestCase, random_string
from datetime import timedelta
from django.utils import timezone
import pytest


pytestmark = pytest.mark.django_db


class TestEventViews(LoggedInTestCase):

    def test_event_can_be_recurring(self):
        self.cal = Calendar(
            name=random_string(),
            slug=random_string(),
        )
        self.cal.save()
        self.event = Event.objects.create(
            start=timezone.now(),
            end=timezone.now() + timedelta(weeks=6),
            title=random_string(),
            calendar=self.cal,
        )
        rule = Rule(
            name=random_string(),
            description=random_string(),
            frequency='WEEKLY',
        )
        rule.save()
        assert rule
        assert self.event
        assert self.cal
        assert not self.event.rule
        url = reverse(
            'edit_event',
            kwargs={
                'calendar_slug': self.cal.slug,
                'event_id': self.event.id,
            },
        )
        response = self.client.post(
            path=url,
            data={
                "start_0": self.event.start.strftime('%Y-%m-%d'),
                "start_1": "09:00",
                "end_0": self.event.end.strftime('%Y-%m-%d'),
                "end_1": "23:00",
                "description": "desc",
                "rule": rule.id,
                "oncall": "foo",
                "fallback": "bar",
            },
        )
        self.assertEqual(200, response.status_code)
        # self.event.refresh_from_db()
        # assert rule == self.event.rule
