#settings for Travis
import sentry_sdk
import os
from .base import *
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = ['46.101.143.60']

SECRET_KEY = os.environ.get('SECRET_KEY', "Q'F?Z'L2?fbgT_-HH${TaZB4")

sentry_sdk.init(
    dsn="https://5f70900d95c14464aa5e14aaac4e0767@o429089.ingest.sentry.io/5375100",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
