# -*- coding: utf-8 -*-
import os
from S3 import CallingFormat


DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False

AWS_ACCESS_KEY_ID = 'AKIAJ6C7XWK5CTIAMC7A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'estagiario-staging'


##########################
##  Amazon S3 Storage   ##
##########################                      
S3_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#S3_FILE_STORAGE = 'storages.backends.s3.S3Storage'
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
AWS_S3_SECURE_URLS = True

STATIC_ROOT = 'static'
STATIC_URL = 'https://s3-sa-east-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = 'media'
MEDIA_URL = 'https://s3-sa-east-1.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


STATICFILES_STORAGE = S3_FILE_STORAGE
DEFAULT_FILE_STORAGE = S3_FILE_STORAGE

AWS_PRELOAD_METADATA = True 

##########################
##        EMAIL         ##
##########################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

DEFAULT_FROM_EMAIL = 'Prova Essa <contato@estagiar.io>'


# Estagiar.io Teste
FACEBOOK_APP_ID = '397248523631923'
FACEBOOK_API_SECRET = 'fcc8abf3f2ff4819b13846bccec20f55'