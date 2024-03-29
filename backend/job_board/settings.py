from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-atd@$h&b!0!^@oyl54=2!pxk0=s1@!xic3zbg4opxkbl&9!-hr"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party app
    "social_django",
    "debug_toolbar",
    "rest_framework_simplejwt",
    "rest_framework",
    "djoser",
    "django_filters",
    # apps
    "core",
    "job",
    "profiles",
]

MIDDLEWARE = [
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "job_board.urls"

CORS_ALLOW_ALL_ORIGINS = True

INTERNAL_IPS = ["127.0.0.1"]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "build")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]


WSGI_APPLICATION = "job_board.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "build/assets")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "core.User"


REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "TOKEN_OBTAIN_SERIALIZER": "core.serializers.TokenObtainPairSerializer",
}


DJOSER = {
    # "LOGIN_FIELD": "email",
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # "SEND_CONFIRMATION_EMAIL": True,
    # "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    # "ACTIVATION_URL": "activate/{uid}/{token}",
    # "SEND_ACTIVATION_EMAIL": True,
    # "SOCIAL_AUTH_TOKEN_STRATEGY": "core.jwt.TokenStrategy",
    # "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
    #     "http://localhost:8000/google",
    # ],
    "SERIALIZERS": {
        "user_create": "core.serializers.UserCreateSerializer",
    },
}

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "eyobm8673@gmail.com"
# EMAIL_HOST_PASSWORD = "jxfp xajc mzhj fnoj"
# EMAIL_USE_TLS = True

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "793352088675-5lkijsbd2tcdahpev0of8imamr8ab94n.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]

SITE_NAME = "http://localhost:5173"
DOMAIN = "localhost:5173"
