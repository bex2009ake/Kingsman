"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8^(ibnfj!oob7&8$lu0h#@ik2-q^$sz=jqvivg25^=gsw-(nnc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # lib
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # app
    'auth_user',
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'moneybusinessdollar@gmail.com'  
EMAIL_HOST_PASSWORD = 'lyat fagm hpnq psyd'  




AUTH_USER_MODEL = 'auth_user.User'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
}




# Настройки Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Настройки для Celery Beat
CELERY_BEAT_SCHEDULE = {
    'task_one': {
        'task': 'auth_user.tasks.check_users',
        'schedule': timedelta(days=1), 
    },
}



# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3ODUyMTA0LCJpYXQiOjE3MTY5ODgxMDQsImp0aSI6ImRmNzkzZTE1NWNiMjRiNmJhZDdkNDJiNjQ3OGU2YzFjIiwidXNlcl9pZCI6MTZ9.s6ZlO02212gA0bUiwh4kCyVyltXc_0hKfv1i-Cut-Eg",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODI4NDEwNCwiaWF0IjoxNzE2OTg4MTA0LCJqdGkiOiJhZjJhMWJiY2U5MGM0NmNjOTg5NjUyNTA1Mzk3MDQ4NiIsInVzZXJfaWQiOjE2fQ.323MT7v7nNCEoBw2rCd9jUjelWG543LHWfCX8zJ1ePU"
# }


# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3OTI3MTQ5LCJpYXQiOjE3MTcwNjMxNDksImp0aSI6IjBkMzEyZDUyMzk4ODQ4YjBiMjAyZjkyOGY0ZDU1ZTdhIiwidXNlcl9pZCI6MTd9.j7P5ESOD1vYHloVK1fr0LNa_LmUgY5205HaGIa2oGX0",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODM1OTE0OSwiaWF0IjoxNzE3MDYzMTQ5LCJqdGkiOiJjZTVjZTRhYjVhNTk0ZWZkODQ1N2ZlNmQxYTVhM2ZhNyIsInVzZXJfaWQiOjE3fQ.OCRMW6OIpQ5hDIyRJje2Z9drrsXMr9SKma8Xva9oLrU"
# }


# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3OTk5ODY1LCJpYXQiOjE3MTcxMzU4NjUsImp0aSI6IjE0YTBhZGY1Y2U0MzQ3NTliNTEyOTZkMGQwNDJmNzExIiwidXNlcl9pZCI6MTh9.FNO6QA2w5eCGQSJtAXzfs8HImtnWnZMCTpG3EQr7FQc",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxODQzMTg2NSwiaWF0IjoxNzE3MTM1ODY1LCJqdGkiOiJhYWE3YWZmNTFjNDU0YTI5OTZmMGYyZjVhMjE0OGQxMiIsInVzZXJfaWQiOjE4fQ.jBbg_rYpAkwRvl1nqImF8C8YhRnQsGSENNattQ30OHY"
# }