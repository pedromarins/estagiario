# -*- coding: utf-8 -*-
from django.db import models
from model_utils import Choices
from address.models import State, City

from datetime import date

class UserProfile(models.Model):
    GENDERS = Choices(['none', 'Nenhum'], ['male', 'Masculino'], ['female', 'Feminio'])

    user        = models.OneToOneField('auth.User')
    
    gender      = models.CharField(choices=GENDERS, default=GENDERS.none, max_length=6)
    birthday    = models.DateField(null=True)

    first_name  = models.CharField(max_length=128, blank=True)
    last_name   = models.CharField(max_length=128, blank=True)
    middle_name = models.CharField(max_length=128, blank=True)
    
    city = models.ForeignKey('address.City', null=True)
    state = models.ForeignKey('address.State', null=True)
    
    #schools
    #workplaces

    class Meta:
        app_label = 'social_user'


from fb_model import UserLanguage, UserEducation, UserWork
import fbdata
def parse_languages(data, user):
    for lang in data.get('languages', []):
        ul = UserLanguage(user=user, name=lang['name'], facebook_id=lang['id'])
        ul.parse_and_save()

def parse_education(data, user):
    for f_ed in data.get('education', []):
        u_ed = UserEducation(user=user)        
        u_ed.kind = f_ed['type']
        
        school = f_ed['school']        
        u_ed.name           = school.get('name', '')
        u_ed.facebook_id    = school.get('id', '')
                
        # concentration           = f_ed.get('concentration', {})
        # u_ed.concentration_id   = concentration.get('id', '')
        # u_ed.concentration_name = concentration.get('name', '')
        
        u_ed.parse_and_save()

def parse_work(data, user):
    for fw in data.get('work', []):
        uw = UserWork(user=user)
        uw.name = fw['employer'].get('name', '')
        uw.facebook_id = fw['employer'].get('id', '')
        uw.parse_and_save()

def fill_profile_from_fb(user, profile, res):
    "fill UserProfile attrs using facebook data"
    
    profile.gender      = res.get('gender', 'none').lower()    
    profile.birthday    = fbdata.get_birthday(res)

    profile.first_name  = res.get('first_name', '')
    profile.middle_name = res.get('middle_name', '')
    profile.last_name   = res.get('last_name', '')
    
    parse_languages(res, user)
    parse_education(res, user)
    parse_work(res, user)

    city, state         = fbdata.get_location(res)
    profile.city        = city
    profile.state       = state

    return profile