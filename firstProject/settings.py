"""
Django settings for firstProject project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import socket

import dj_database_url
from pathlib import Path
import django
from django.utils.encoding import smart_str
from dotenv import load_dotenv
from google.oauth2 import service_account


django.utils.encoding.smart_text = smart_str

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
LOCAL = True

if LOCAL:
    load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')


ALLOWED_HOSTS = [
                '127.0.0.1',
                'apparel-shop1.onrender.com',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'firstProject.web',
    'firstProject.accounts',
    
    'rest_framework',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firstProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'firstProject.utilities.context_processors.categories_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'firstProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.parse('postgres://render_db_zrws_user:KTbKd8jx92OGh4DTBEOqsX3lvRrc488q@dpg-cfkibnhmbjsn9ecjuigg-a.frankfurt-postgres.render.com/render_db_zrws')
# }

# DATABASES = {
#     'default': dj_database_url.parse(f'postgres://render_db_zrws_user:{os.environ.get("DB_PASSWORD")}@dpg-cfkibnhmbjsn9ecjuigg-a.frankfurt-postgres.render.com/render_db_zrws')
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'first_project',
        'USER': 'postgres',
        'PASSWORD': '1123QwER',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_BUCKET_NAME = 'user-uploaded-images_apparelshop1'
GS_PROJECT_ID = 'apparelshop1'
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file('/etc/secrets/apparelshop1-c54be055c23b.json')



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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
#     BASE_DIR / 'templates'
# ]


# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.FirstProjectUser'

MEDIA_URL = 'https://storage.googleapis.com/user-uploaded-images_apparelshop1/'

#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')

LOGIN_REDIRECT_URL = '/'

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'apparelshop1-c54be055c23b.json'
