import pytest
from unittest.mock import patch
from rest_framework import status
from django.urls import reverse
from apps.incidents.models import Incident, IncidentSilenced
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_silence_incident_incident_not_found(mocked_messages_error, authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": base_user.id,
        "silence_for": 4,
    }
    url = reverse('incidents_silence', kwargs={'incident_id': 0})
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 0
    assert mocked_messages_error.called


@pytest.mark.django_db
def test_post_silence_incident(authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": base_user.id,
        "silence_for": 4,
    }
    url = reverse('incidents_silence', kwargs={'incident_id': incident.id})
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 1


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_unsilence_incident_incident_not_found(mocked_messages_error, authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
    }
    url = reverse('incidents_unsilence', kwargs={'incident_id': 0})
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 0
    assert mocked_messages_error.called


@pytest.mark.django_db
def test_post_unsilence_incident(authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
    }
    url = reverse('incidents_unsilence', kwargs={'incident_id': incident.id})
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 1


@pytest.mark.django_db
def test_post_silence_incident_with_silenced_incident(authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    G(IncidentSilenced, incident=incident)
    data = {
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": base_user.id,
        "silence_for": 4,
    }
    url = reverse('incidents_silence', kwargs={'incident_id': incident.id})
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 0
