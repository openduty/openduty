import pytest
from unittest.mock import patch
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from rest_framework import status
from apps.commons.tests.fixtures import admin_user
from apps.accounts.views import UserEditView


@pytest.mark.django_db
def test_user_create(admin_user):
    data = {
        "user-username": "usertest",
        "user-password": "1234test",
        "user-email": "test@test.com",
        "profile-phone_number": "1234567890",
        "profile-pushover_user_key": "1234567890",
        "profile-pushover_app_key": "1234567890",
        "profile-slack_room_name": "1234567890",
        "profile-prowl_api_key": "1234567890",
        "profile-prowl_application": "1234567890",
        "profile-prowl_url": "1234567890",
        "profile-rocket_webhook_url": "1234567890",
        "profile-hipchat_room_name": "room",
        "profile-hipchat_room_url": "1234567890"
    }
    assert User.objects.count() == 1
    create_user_url = reverse('UserCreateView')
    client = Client()
    client.force_login(admin_user)
    response = client.post(create_user_url, data)
    assert response.status_code == status.HTTP_302_FOUND
    assert User.objects.count() == 2
    get_response = client.get(create_user_url)
    assert get_response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@patch('django.http.request')
def test_user_update(mocked_request, admin_user):
    data = {
        "user-username": "usertest",
        "user-password": "1234test",
        "user-email": "test@test.com",
        "profile-phone_number": "1234567890",
        "profile-pushover_user_key": "1234567890",
        "profile-pushover_app_key": "1234567890",
        "profile-slack_room_name": "1234567890",
        "profile-prowl_api_key": "1234567890",
        "profile-prowl_application": "1234567890",
        "profile-prowl_url": "1234567890",
        "profile-rocket_webhook_url": "1234567890",
        "profile-hipchat_room_name": "room",
        "profile-hipchat_room_url": "1234567890"
    }
    assert User.objects.count() == 1
    kwargs = {"pk": admin_user.id}
    edit_user_url = reverse('UserEditView', kwargs=kwargs)
    client = Client()
    client.force_login(admin_user)
    response = client.post(edit_user_url, data)
    assert response.status_code == status.HTTP_302_FOUND
    assert User.objects.count() == 1

    get_response = client.get(edit_user_url)
    view = UserEditView()
    view.object = admin_user
    view.request = mocked_request
    assert get_response.status_code == status.HTTP_302_FOUND
    assert view.get_context_data()


@pytest.mark.django_db
def test_save(admin_user):
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
        "hipchat_room_name": "room",
        "hipchat_room_url": "1234567890"
    }
    assert User.objects.count() == 1
    create_user_url = reverse('openduty.users.save')
    client = Client()
    client.force_login(admin_user)
    response = client.post(create_user_url, data)
    assert response.status_code == status.HTTP_302_FOUND

