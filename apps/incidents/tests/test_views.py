import pytest
from unittest.mock import patch
from rest_framework import status
from django.urls import reverse
from apps.incidents.models import Incident, IncidentSilenced, Service
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
def test_get_incident_detail(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    response = c.get(reverse('IncidentDetailView', args=[incident.id]))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_incident_detail_with_incident_silenced(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    incident_silenced = G(IncidentSilenced, incident=incident)
    response = c.get(reverse('IncidentDetailView', args=[incident.id]))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_incidents_list_on_call(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    response = c.get(reverse('OnCallIncidentsListView'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_incidents_list(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    response = c.get(reverse('IncidentsListView'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_update_type(authenticated_client):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    new_event_type = Incident.RESOLVE
    data = {
        'id': str(incident.id),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        'event_type': new_event_type
    }
    url = reverse('incidents_update_type')
    response = c.post(
        url, data, format='json'
    )
    assert response.status_code == status.HTTP_302_FOUND
    incident.refresh_from_db()
    assert incident.event_type == new_event_type


@pytest.mark.django_db
def test_update_type(base_user):
    service = G(Service)
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE, service_to_escalate_to=service)
    new_event_type = Incident.RESOLVE
    from apps.incidents.views import _update_type
    _update_type(user=base_user, ids=[incident.id], event_type=new_event_type)
    incident.refresh_from_db()
    assert incident.event_type == new_event_type


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_update_type_event_type_is_none(mocked_messages_error, authenticated_client):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    new_event_type = Incident.RESOLVE
    data = {
        'id': str(incident.id),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        # 'event_type':
    }
    url = reverse('incidents_update_type')
    response = c.post(
        url, data, format='json'
    )
    assert response.status_code == status.HTTP_302_FOUND
    incident.refresh_from_db()
    assert incident.event_type == Incident.ACKNOWLEDGE
    assert mocked_messages_error.called


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_update_type_incident_not_found(mocked_messages_error, authenticated_client):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    new_event_type = Incident.RESOLVE
    data = {
        'id': str(incident.id + 1),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        'event_type': new_event_type
    }
    url = reverse('incidents_update_type')
    response = c.post(
        url, data, format='json'
    )
    assert response.status_code == status.HTTP_302_FOUND
    incident.refresh_from_db()
    assert incident.event_type == Incident.ACKNOWLEDGE
    assert mocked_messages_error.called


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_update_type_from_resolved_back_acknowledge(mocked_messages_error, authenticated_client):
    c = authenticated_client
    new_event_type = Incident.RESOLVE
    incident = G(Incident, event_type=new_event_type)
    data = {
        'id': str(incident.id),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        'event_type': Incident.ACKNOWLEDGE
    }
    url = reverse('incidents_update_type')
    response = c.post(
        url, data, format='json'
    )
    assert response.status_code == status.HTTP_302_FOUND
    incident.refresh_from_db()
    assert incident.event_type == new_event_type
    assert mocked_messages_error.called


@pytest.mark.django_db
def test_post_forward_incident(authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'id': str(incident.id),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": base_user.id
    }
    url = reverse('incidents_forward_incident')
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 1


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_forward_incident_user_not_found(mocked_messages_error, authenticated_client):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'id': str(incident.id),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": 0
    }
    url = reverse('incidents_forward_incident')
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 0
    assert mocked_messages_error.called


@pytest.mark.django_db
@patch('django.contrib.messages.error')
def test_post_forward_incident_incident_not_found(mocked_messages_error, authenticated_client, base_user):
    c = authenticated_client
    incident = G(Incident, event_type=Incident.ACKNOWLEDGE)
    data = {
        'id': str(incident.id + 1),
        'url': str(reverse('IncidentDetailView', args=[incident.id])),
        "user_id": base_user.id
    }
    url = reverse('incidents_forward_incident')
    response = c.post(url, data, format='json')
    assert response.status_code == status.HTTP_302_FOUND
    assert incident.eventlog_set.count() == 0
    assert mocked_messages_error.called


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
@patch('django.contrib.messages.error')
def test_post_silence_incident(mocked_messages_error, authenticated_client, base_user):
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
@patch('django.contrib.messages.error')
def test_post_unsilence_incident(mocked_messages_error, authenticated_client, base_user):
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
