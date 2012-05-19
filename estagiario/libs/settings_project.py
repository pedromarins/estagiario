# -*- coding: utf-8 -*-


### FACEBOOK ###
# https://developers.facebook.com/docs/authentication/permissions/
EXTENDED_PERMISSIONS = [    
    'email',
    'publish_stream', 
    'user_location',            'friends_location',
    'user_work_history'         'friends_work_history',    
    'user_education_history',   'friends_education_history',
]

#FACEBOOK_EXTENDED_PERMISSIONS = EXTENDED_PERMISSIONS


FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_location', 'user_work_history', 'user_education_history', 'publish_stream', 'user_birthday']
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

#Social Auth
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'


SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_user.pipeline.populate_user_profile',
)


# Number of search results shown to anonymous users 
ANON_RESULTS_COUNT = 6


CSS = {
    'field_menu_active': 'active',
}