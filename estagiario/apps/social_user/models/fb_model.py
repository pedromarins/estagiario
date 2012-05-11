# -*- coding: utf-8 -*-
from django.db import models


class FacebookModel(models.Model):
    facebook_id = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    
    __unicode__ = lambda x: x.name

    class Meta:
        abstract = True
        app_label = 'social_user'

    def _validate_attrs(self):
        "Validates required attributes"
        if not self.user:
            raise Exception('self.user is required')

        if not self.facebook_id:
            raise Exception('self.facebook_id is required')

        if not self.name:
            raise Exception('self.name is required')

    def parse_and_save(self):
        "save if it doesnt exist"
        self._validate_attrs()
        try:
            self.save()
            return self
        except Exception:
            return None




class UserLanguage(FacebookModel):
    "Facebook Language objects"  
    user = models.ForeignKey('auth.User', related_name='languages')

    class Meta:
        app_label = 'social_user'
        unique_together = ('user', 'facebook_id')

    @classmethod
    def unique_save(cls, user, name, fb_id):
        try:
            ul = cls.objects.create(user=user, name=name, facebook_id=fb_id)
        except Exception:
            pass


class UserEducation(FacebookModel):
    "Facebook Education objects"  
    user = models.ForeignKey('auth.User', related_name='schools')
    kind = models.CharField(max_length=64, blank=True)
    
    concentration_name  = models.CharField(max_length=128)
    concentration_id    = models.CharField(max_length=128)

    class Meta:
        app_label = 'social_user'
        unique_together = ('user', 'facebook_id')



class UserWork(FacebookModel):
    "Facebook Education objects"  
    user = models.ForeignKey('auth.User', related_name='workplaces')
    
    class Meta:
        app_label = 'social_user'
        unique_together = ('user', 'facebook_id')
