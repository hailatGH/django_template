import os
from config.settings.base import *

SECRET_KEY = os.getenv("SECRET_KEY", None)
DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(
    ","
)  # Comma-separated list of allowed hosts

# Application definition
INSTALLED_APPS += [
    # Third-party apps
    "rest_framework",  # Django REST framework
    "corsheaders",  # CORS headers
    "django_filters",  # Django filters
]

# Middleware configuration
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.common.CommonMiddleware"),
    "corsheaders.middleware.CorsMiddleware",
)

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": int(os.getenv("POSTGRES_PORT")),
    }
}

# Static and media files configuration
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "https://production-domain.com",  # Replace with production domain
]

CSRF_TRUSTED_ORIGINS = [
    "https://production-domain.com",  # Replace with production domain
]

# Django Rest Framework configuration
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}
