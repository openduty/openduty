import pytest
from rest_framework import status
from django.urls import reverse
from apps.incidents.models import Incident, IncidentSilenced
from django_dynamic_fixture import G
from apps.commons.tests.fixtures import authenticated_client, base_user, other_user


@pytest.mark.django_db
def test_get_incident_detail(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    response = c.get(reverse('incident_details', args=[incident.id]))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_incident_detail_with_incident_silenced(authenticated_client):
    c = authenticated_client
    incident = G(Incident)
    incident_silenced = G(IncidentSilenced, incident=incident)
    response = c.get(reverse('incident_details', args=[incident.id]))
    assert response.status_code == status.HTTP_200_OK
