import pytest

from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from always_authenticated.middleware import AlwaysAuthenticatedMiddleware

@pytest.mark.django_db
def test_ok(client):
    response = client.get('/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_creates_user(client):
    """
    Tests that making an unauthenticated request creates a user.
    """
    assert not User.objects.exists()
    response = client.get('/')

    assert User.objects.count() == 1
    assert response.status_code == 200
    assert response.wsgi_request.user.username == 'user'

def test_debug_false_raises_exception(settings):
    """
    Tests that the middleware raises an exception when DEBUG is set to False.
    """
    settings.DEBUG = False

    with pytest.raises(ImproperlyConfigured):
        AlwaysAuthenticatedMiddleware()


def test_debug_only_setting(settings):
    """
    Tests that the middleware doesn't raise an exception when DEBUG is set to
    False when ALWAYS_AUTHENTICATED_DEBUG_ONLY is set to False.
    """
    settings.DEBUG = False
    settings.ALWAYS_AUTHENTICATED_DEBUG_ONLY = False

    AlwaysAuthenticatedMiddleware()


@pytest.mark.django_db
def test_username_setting(settings, client):
    settings.ALWAYS_AUTHENTICATED_USERNAME = 'testuser'

    response = client.get('/')

    assert response.status_code == 200
    assert response.wsgi_request.user.username == 'testuser'


@pytest.mark.django_db
def test_user_defaults_setting(settings, client):
    settings.ALWAYS_AUTHENTICATED_USER_DEFAULTS = {
        'email': 'testuser@example.com'
    }

    response = client.get('/')

    assert response.status_code == 200
    assert response.wsgi_request.user.email == 'testuser@example.com'
