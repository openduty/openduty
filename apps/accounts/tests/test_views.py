import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from rest_framework import status
from apps.commons.tests.fixtures import admin_user


@pytest.mark.django_db
def test_user_create(admin_user):
    data = {
        "id": admin_user.id,
        "username": "usertest",
        "password": "1234test",
        "email": "test@test.com",
        "phone_number": "1234567890",
        "pushover_user_key": "1234567890",
        "pushover_app_key": "1234567890",
        "slack_room_name": "1234567890",
        "prowl_api_key": "1234567890",
        "prowl_application": "1234567890",
        "prowl_url": "1234567890",
        "rocket_webhook_url": "1234567890",
        "hipchat_room_name": "1234567890",
        "hipchat_room_url": "1234567890"
    }
    create_user_url = reverse('openduty.users.save')
    client = Client()
    client.force_login(admin_user)
    response = client.post(create_user_url, data)
    assert response.status_code == status.HTTP_302_FOUND
    assert User.objects.count() == 1
