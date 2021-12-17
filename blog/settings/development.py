from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

DJANGO_APPS += []

THIRD_PARTY_APPS = [
    "rest_framework",
    # "rest_framework.authtoken",
    # "allauth",
    # "allauth.account",
    # "dj_rest_auth",
    # "dj_rest_auth.registration",
    # "rest_framework_simplejwt.token_blacklist",
]

LOCAL_APPS = ["apps.common", "apps.users", "apps.posts",]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}