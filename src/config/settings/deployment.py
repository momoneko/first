from config.settings.base import *  # flake8: noqa

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '*',
]

STATIC_ROOT = "/var/www/my_project/static/"
MEDIA_ROOT = "/var/www/my_project/media/"
