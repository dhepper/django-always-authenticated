===========================
Django Always Authenticated
===========================

A middleware that ensures that a request always has an authenticated user.

If the request doesn't have an authenticated user, it logs in a default
user. If the default user doesn't exist, it is created.

Compatibility
=============
This middleware has been tested with these versions of Django:

* 1.7
* 1.8
* 1.9
* 1.10
* master (at the time of the release)

Setup
=====

Install from PyPI::

    pip install django_always_authenticated

Add to ``MIDDLEWARE`` (``MIDDLEWARE_CLASSES`` for Django <1.10) in settings file::

    MIDDLEWARE = (
        ...
        'always_authenticated.middleware.AlwaysAuthenticatedMiddleware',
    )

As a security safeguard, the middleware will raise an
``ImproperlyConfiguredException`` when running in production mode
(``DEBUG=False``).
To run the middleware in production, set ``ALWAYS_AUTHENTICATED_DEBUG_ONLY`` to
``False``.

Configuration
=============

This middleware reads these settings:

ALWAYS_AUTHENTICATED_USERNAME
-----------------------------
A string with the name of the default user, defaults to ``'user'``.

ALWAYS_AUTHENTICATED_USER_DEFAULTS
----------------------------------
A dict with additional default values to set when creating the user.

ALWAYS_AUTHENTICATED_DEBUG_ONLY
-------------------------------
Set to `False` to allow running with DEBUG=False.

Example project
===============
There is a very single example project that demonstrates the middleware in the
directory `example_project`.

Running Tests
=============
To run the tests, install the requirements and run py.test::

    pip install -r requirements.txt
    py.test

You can also use tox to run the tests with all supported versions of
Python and Django::

    pip install tox
    tox
