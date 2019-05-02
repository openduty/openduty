import pytest
from unittest.mock import patch
from rest_framework import status
from apps.accounts.models import Token
from apps.services.models import ServiceTokens, Service
from apps.incidents.models import Incident
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
def test_port_incidents_over_api_no_service_key(authenticated_client):
    c = authenticated_client
    url = '/api/create_event/'
    token_key = 'no_valid_dummy_key'
    incident_key = 'incident_key'
    event_type = "wrong key"
    response = c.post(
        url,
        {
            'name': 'Incident',
            'service_key': token_key,
            'incident_key': incident_key,
            'event_type': event_type,
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {'No service key'}


@pytest.mark.django_db
def test_port_incidents_over_api_service_key_not_found(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = "wrong key"
    G(Token, key=token_key)
    url = '/api/create_event/'
    response = c.post(
        url,
        {
            'service_key': token_key,
            'incident_key': incident_key,
            'event_type': event_type,
        },
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


@pytest.mark.django_db
def test_create_event_is_clean(authenticated_client):
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
def test_create_event_no_keys(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(Incident, incident_key=incident_key, event_type=Incident.ACKNOWLEDGE)
    url = '/api/create_event/'
    data = {
        # 'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    expected_response = {
        "status": "failure",
        "message": "Mandatory parameter missing"
    }
    assert response.data == expected_response

    data = {
        'service_key': token_key,
        # 'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == expected_response

    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        # 'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_event_no_event_type(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = "invalid one"
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    # incident = G(Incident, incident_key=incident_key, event_type=Incident.ACKNOWLEDGE)
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_event_incident_already_existent(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=incident_key,
        event_type=Incident.ACKNOWLEDGE,
        service_key=service
    )
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_event_incident_already_existent_unescalated(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=incident_key,
        event_type=Incident.TRIGGER,
        service_key=service
    )
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_event__is_not_clean(authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=incident_key,
        event_type=event_type,
        service_key=service
    )
    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
@patch('apps.notification.helper.NotificationHelper.notify_incident')
def test_create_event_is_to_resolve(mocked_send_notifications, authenticated_client):
    c = authenticated_client
    token_key = 'dummy_key'
    incident_key = 'incident_key'
    event_type = Incident.RESOLVE
    token = G(Token, key=token_key)
    service = G(Service, send_resolve_enabled=True)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=incident_key,
        event_type=Incident.RESOLVE,
        service_key=service
    )

    url = '/api/create_event/'
    data = {
        'service_key': token_key,
        'incident_key': incident_key,
        'event_type': event_type,
    }
    response = c.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert mocked_send_notifications.called


@pytest.mark.django_db
def test_update_event_no_service(authenticated_client):
    c = authenticated_client
    event_type = Incident.ACKNOWLEDGE
    incident = G(Incident)
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key":  "test_service_key",
        "incident_key":  "test_service_key",
        "event_type":  event_type,
        "description": "description",
        "details": "details"
    }
    response = c.put(url, data, content_type='application/json')
    expected_response = {"No service key"}
    assert response.data == expected_response
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_update_event_service_key_not_found(authenticated_client):
    import uuid
    c = authenticated_client
    good_token_key = str(uuid.uuid4())
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=good_token_key)
    service = G(Service)
    incident = G(
        Incident,
        event_type=event_type,
        service_key=service
    )
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key": str(token.key),
        "incident_key":  "test_service_key",
        "event_type":  event_type,
        "description": "description",
        "details": "details"
    }
    response = c.put(url, data, content_type='application/json')
    expected_response = {"Service key does not exist"}
    assert response.data == expected_response
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_update_event_service_no_service_to_escalate_to(authenticated_client):
    import uuid
    c = authenticated_client
    good_token_key = str(uuid.uuid4())
    event_type = Incident.ACKNOWLEDGE
    token = G(Token, key=good_token_key)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=good_token_key,
        event_type=event_type,
        service_key=service
    )
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key": str(good_token_key),
        "incident_key":  "test_service_key",
        "event_type":  event_type,
        "description": "description",
        "details": "details"
    }
    response = c.put(url, data, content_type='application/json')
    expected_response = {"No service to escalate to key"}
    assert response.data == expected_response
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_update_event_service_service_to_escalate_key_not_found(authenticated_client):
    c = authenticated_client
    event_type = Incident.ACKNOWLEDGE
    token = G(Token)
    token2 = G(Token)
    service = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    incident = G(
        Incident,
        incident_key=str(token.key),
        event_type=event_type,
        service_key=service,
        service_to_escalate_to=service,
    )
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key": str(token.key),
        "incident_key":  "test_service_key",
        "event_type":  event_type,
        "description": "description",
        "details": "details",
        "service_key_to_escalate_to": str(token2.key),
    }
    response = c.put(url, data, content_type='application/json')
    expected_response = {"Service to escalate to key does not exist"}
    assert response.data == expected_response
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_update_event_service(authenticated_client):
    c = authenticated_client
    event_type = Incident.RESOLVE
    token = G(Token)
    token2 = G(Token)
    service = G(Service)
    service2 = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    G(ServiceTokens, service_id=service2, token_id=token2)
    incident = G(
        Incident,
        incident_key=str(token.key),
        event_type=Incident.ACKNOWLEDGE,
        service_key=service,
        service_to_escalate_to=service,
    )
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key": str(token.key),
        "incident_key": str(token.key),
        "incident_details": "incident_details",
        "event_type":  event_type,
        "description": "description",
        "details": "details",
        "service_key_to_escalate_to": str(token2.key),
    }
    response = c.put(url, data, content_type='application/json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_event_service_incident_not_found(authenticated_client):
    c = authenticated_client
    event_type = Incident.RESOLVE
    token = G(Token)
    token2 = G(Token)
    service = G(Service)
    service2 = G(Service)
    G(ServiceTokens, service_id=service, token_id=token)
    G(ServiceTokens, service_id=service2, token_id=token2)
    incident = G(
        Incident,
        incident_key=str(token.key),
        event_type=Incident.ACKNOWLEDGE,
        service_key=service,
        service_to_escalate_to=service,
    )
    url = f"/api/create_event/{incident.id}/escalate/"
    data = {
        "service_key": str(token.key),
        "incident_key": str(token2.key),
        "incident_details": "incident_details",
        "event_type":  event_type,
        "description": "description",
        "details": "details",
        "service_key_to_escalate_to": str(token2.key),
    }
    response = c.put(url, data, content_type='application/json')
    expected_response = {'Incident does not exist'}
    assert response.data == expected_response
    assert response.status_code == status.HTTP_404_NOT_FOUND
