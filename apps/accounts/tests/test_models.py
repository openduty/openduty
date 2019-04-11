import pytest
from django.contrib.auth.models import User
from apps.accounts.models import Token


@pytest.mark.django_db
@pytest.fixture
def base_user():
    user = User.objects.create_user(
        email='regular_user@example.com',
        username='regular_user',
        password='1234test'
    )
    return user


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        email='regular_user@example.com',
        username='regular_user',
        password='1234test'
    )
    assert user.pk


def test_token_generate_key():
    token = Token()
    key = token.generate_key()
    assert key
    assert len(key) == 40, "Should return a 40 charachers string: hexdigest()"


@pytest.mark.django_db
def test_token_save():
    token = Token()
    token.save()
    assert token.key
    assert len(token.key) == 40, "Should return a 40 charachers key"


@pytest.mark.django_db
def test_token___unicode__str__():
    token = Token()
    token.save()
    assert token.key == token.__unicode__()
    assert token.key == token.__str__()
    assert token.__str__() == token.__unicode__()
