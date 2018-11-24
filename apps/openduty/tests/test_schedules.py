from django.urls import reverse
from schedule.models import Calendar
from apps.openduty.tests.shared import LoggedInTestCase, random_string
import pytest

pytestmark = pytest.mark.django_db


class TestSchedulesViews(LoggedInTestCase):

    def setUp(self):
        super(TestSchedulesViews, self).setUp()
        self.cal = Calendar(
            name=random_string(),
            slug=random_string(),
        )
        self.cal.save()

    def tearDown(self):
        super(TestSchedulesViews, self).tearDown()
        try:
            self.cal.delete()
        except Exception:
            pass

    @pytest.mark.skip(reason="TO Be Fixed")
    def test_schedule_detail_view_works_with_query_args(self):
        assert self.cal.id
        response = self.client.get(
            reverse('calendar_details', args=[self.cal.slug]),
            {'month': '11', 'year': '2014'},
        )
        self.assertEqual(response.status_code, 200)
