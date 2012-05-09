# -*- coding: utf-8 -*-

import os
import sys
from settings_helper import add_sys_path, Path

PATH = Path(__file__)

add_sys_path(PATH.PROJECT, 'apps')
add_sys_path(PATH.PROJECT, 'libs')


SECRET_KEY = 'wm0h0mzavxh0-$h#9^03!kfu9*u4veknx3bguc8nswf0brfi'

ADMINS = ( ('Victor', 'victor@sparkit.com.br'), )
MANAGERS = ADMINS


TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
USE_I18N = True
USE_L10N = True
USE_TZ = True   ##S3


ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'


STATICFILES_DIRS = ( PATH.local('static'), )
TEMPLATE_DIRS = ( PATH.local('templates') )
FIXTURE_DIRS = ( PATH.local('static'), )


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'core.middleware.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gunicorn',

    'core',
)


ENV = os.environ.get('ENV', 'dev')

if ENV == 'production':
    from libs.settings_production import *

elif ENV == 'staging':    
    from libs.settings_staging import *

else:
    from libs.settings_dev import *

