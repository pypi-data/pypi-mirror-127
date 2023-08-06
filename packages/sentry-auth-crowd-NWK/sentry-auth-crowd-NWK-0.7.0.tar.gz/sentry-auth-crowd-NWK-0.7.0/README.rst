Crowd Auth Backend for Sentry
=============================

A Crowd authentication backend for Sentry.

Original code written by TRBS. All credits go to him.

Succesfully updated and applied to Sentry 21.9.0 by NWK.

Install
-------

.. code-block:: console

    $ pip install sentry-auth-crowd-NWK

If you are using `getsentry/onpremise`_ to install sentry, just add `sentry-auth-crowd-NWK` in getsentry/onpremise/requirements.txt .

Setup
-----

In Atlassian Crowd create an application for Sentry we will need the
application name and password for the Sentry configuration.

Make sure the remote addresses are set correct to avoid authentication failures.
E.g. remember to add localhost to Remote adresses if Crowd server runs a reverse proxy.

The following settings should be set in ``sentry.conf.py``:

.. code-block:: python

    # Url of the Crowd server
    CROWD_URL = ""
    # The application name of Sentry in Crowd
    CROWD_APP_NAME = ""
    # The application password of Sentry in Crowd
    CROWD_APP_PASSWORD = ""
    # Put this after AUTHENTICATION_BACKENDS declaration, if it not exists, just set
    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
        'sentry_auth_crowd.backend.SentryCrowdBackend',
    )
    
If you are using `getsentry/onpremise`_ to install sentry, after done above, remember to rerun install script

*./install.sh* 

then 

*docker-compose up -d*

now enjoy it!

.. _getsentry/onpremise: https://github.com/getsentry/onpremise 

