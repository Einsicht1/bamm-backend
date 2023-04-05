from .base import *

DEBUG = False

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
DEFAULT_FILE_STORAGE = 'bamm.storage_backends.MediaStorage'
STATICFILES_STORAGE = 'bamm.storage_backends.StaticStorage'

DATABASES = {
    "default": {"ENGINE": os.environ.get("ENGINE"),
                "NAME": os.environ.get("NAME"),
                "HOST": os.environ.get("HOST"),
                "PORT": os.environ.get("PORT"),
                "USER": os.environ.get("USER"),
                "PASSWORD": os.environ.get("PASSWORD")
                }

}
print(DATABASES)
