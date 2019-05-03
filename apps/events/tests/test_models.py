import pytest
from django_dynamic_fixture import G
from apps.events.models import EventLog
from apps.services.models import Service


@pytest.mark.django_db
def test_create_event_log():
    data = "DATA"
    action = 'acknowledge'
    service_key = G(Service)
    event_log = G(
        EventLog,
        data=data,
        action=action,
        service_key=service_key
    )
    assert event_log.pk
    assert event_log.color == 'warning'
    assert event_log.__str__() == data
    assert event_log.natural_key() == (service_key, event_log.id)
