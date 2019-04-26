import pytest
import string
import random
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django_dynamic_fixture import G
from rest_framework.test import APIRequestFactory
from apps.accounts.models import Profile


@pytest.mark.django_db
@pytest.fixture
def base_user():
    user = User.objects.create_user(
        email='regular_user@example.com',
        username='regular_user',
        password='1234test'
    )
    G(Profile, user=user)
    return user


@pytest.mark.django_db
@pytest.fixture
def other_user():
    user = User.objects.create_user(
        email='other_user@example.com',
        username="other_user",
        password='1234test'
    )
    G(Profile, user=user)
    return user


@pytest.mark.django_db
@pytest.fixture
def admin_user():
    user = User.objects.create_superuser(
        email='admin_user@example.com',
        username="admin_user",
        password='1234test'
    )
    G(Profile, user=user)
    return user


@pytest.mark.django_db
@pytest.fixture
def authenticated_client():
    user = User.objects.create_superuser(
        email='admin_user@example.com',
        username="admin_user",
        password='1234test'
    )
    G(Profile, user=user)
    client = Client()
    client.force_login(user)
    return client


@pytest.fixture
def create_view(view_class, url,  url_kwargs, payload=None, action_map=None, request_user=None):
    request_type, method_called = None, None
    for key, val in action_map.items():
        request_type, method_called = key, val
    if request_type == 'get':
        request = APIRequestFactory().get(url, format='json')
    elif request_type == 'post':
        request = APIRequestFactory().post(url, data=payload, format='json')
    elif request_type == 'put':
        request = APIRequestFactory().put(url, data=payload, format='json')
    elif request_type == 'patch':
        request = APIRequestFactory().patch(url, data=payload, format='json')
    elif request_type == 'delete':
        request = APIRequestFactory().delete(url, format='json')
    else:
        request = APIRequestFactory().get(url, format='json')
    if request_user:
        request.user = request_user
    else:
        request.user = AnonymousUser()
    request.kwargs = url_kwargs
    request.data = payload
    instantiated_view_class = view_class()
    instantiated_view_class.action_map = action_map
    instantiated_view_class.dispatch(request, **url_kwargs)

    if method_called == 'list':
        response = instantiated_view_class.list(request, **url_kwargs)
    elif method_called == 'retrieve':
        response = instantiated_view_class.retrieve(request, **url_kwargs)
    elif method_called == 'update':
        response = instantiated_view_class.update(request, **url_kwargs)
    elif method_called == 'partial_update':
        response = instantiated_view_class.partial_update(request, **url_kwargs)
    elif method_called == 'delete':
        response = instantiated_view_class.delete(request, **url_kwargs)
    else:
        response = instantiated_view_class.list(request, **url_kwargs)
    return response


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class BaseTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.username = random_string()
        cls.password = random_string()
        cls.user = User.objects.create_superuser(
            cls.username,
            'test@localhost',
            cls.password,
        )

    @classmethod
    def tearDownClass(cls):
        try:
            cls.user.delete()
        except Exception:
            pass


class LoggedInTestCase(BaseTestCase):

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.user)
