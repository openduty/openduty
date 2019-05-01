import pytest
from django.core.exceptions import ValidationError
from django_dynamic_fixture import G
from apps.incidents.models import Incident, IncidentSilenced, Service


@pytest.mark.django_db
def test_create_incident():
    incident_key = "KEY"
    incident = G(
        Incident,
        event_type='acknowledge',
        incident_key=incident_key
    )
    assert incident.pk
    assert incident.color == 'warning'
    assert incident.__str__() == incident_key


@pytest.mark.django_db
def test_incident_natural_key():
    incident_key = "KEY"
    service_key = G(Service)
    incident = G(
        Incident,
        event_type='acknowledge',
        incident_key=incident_key,
        service_key=service_key
    )
    assert incident.pk
    assert service_key in incident.natural_key()
    assert incident_key in incident.natural_key()


@pytest.mark.django_db
def test_incident_clean():
    event_type = "EVENT_TYPE"
    incident = G(
        Incident,
        event_type=event_type,
    )
    with pytest.raises(ValidationError) as error:
        assert incident.clean() == error
