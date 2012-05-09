# -*- coding: utf-8 -*-

from settings_helper import get_path
from settings import PATH

SITE_ID = 1 

DEBUG = True
TEMPLATE_DEBUG = True


##########################
##        ASSETS        ##
##########################
STATIC_ROOT = get_path('static_root')
STATIC_URL = '/static/'
MEDIA_ROOT = get_path('media')
#MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"



DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': get_path('db.sqlite'), } }


DEFAULT_FROM_EMAIL = 'Victor <victor@sparkit.com.br>'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


##########################
##       LOGGING        ##
##########################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PATH.local('db.sqlite'),
        'USER': '','PASSWORD': '','HOST': '','PORT': '',
    }
}


