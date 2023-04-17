import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
DEFAULT_FILE_STORAGE = "bamm.storage_backends.MediaStorage"
STATICFILES_STORAGE = "bamm.storage_backends.StaticStorage"

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("ENGINE"),
        "NAME": os.environ.get("NAME"),
        "HOST": os.environ.get("HOST"),
        "PORT": os.environ.get("PORT"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
    }
}


sentry_sdk.init(
    dsn="https://e33994c42b764c48bd44215bac0d1a09@o4504989486809088.ingest.sentry.io/4504989492838400",
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
    environment="production",
)
