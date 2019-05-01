import pytest
from rest_framework import status
from apps.accounts.models import Token
from apps.services.models import ServiceTokens, Service
from apps.incidents.models import Incident
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from django_dynamic_fixture import G
from schedule.models import Calendar, Event
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
def test_port_incidents_over_api_no_service_key(authenticated_client):
    c = authenticated_client
    url = '/api/create_event/'
    response = c.post(
        url,
        {'name': 'Incident'},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {'No service key'}


@pytest.mark.django_db
def test_port_incidents_over_api_service_key_not_found(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    G(Token, key=token_key)
    url = '/api/create_event/'
    response = c.post(
        url,
        {'service_key': token_key},
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {'Service key does not exist'}


@pytest.mark.django_db
def test_create_event(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.ESCALATE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(Incident, incident_key=incident_key)
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    expected_response = {
        'status': 'success',
        'message': 'Event processed',
        'incident_key': 'incident_key'
    }
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_event_invalid_event_type(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.RESOLVE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(Incident, incident_key=incident_key, event_type=event_type)
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    expected_response = {
        'status': 'success',
        'message': 'Event processed',
        'incident_key': 'incident_key'
    }
    assert response.data == expected_response


