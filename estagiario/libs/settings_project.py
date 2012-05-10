# -*- coding: utf-8 -*-


### FACEBOOK ###
# https://developers.facebook.com/docs/authentication/permissions/
FACEBOOK_EXTENDED_PERMISSIONS = [    
    'email',
    'publish_stream', 
    'user_location'             'friends_location',
    'user_work_history'         'friends_work_history',    
    'user_education_history',   'friends_education_history',
]





LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

#Social Auth
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
