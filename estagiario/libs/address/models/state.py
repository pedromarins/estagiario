# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Count
from django.db.models.query import QuerySet

from model_utils.managers import PassThroughManager
from django.db.models import get_model


class StateQuerySet(QuerySet):
    def _states_with_internships_ids(self):
        return get_model('internships', 'Internship').objects.available().values_list('state__id', flat=True).distinct()
    
    def has_internship(self):
        "states with available internships ordered by descending internship count"
        active_states = self._states_with_internships_ids()
        return self.filter(id__in=active_states).annotate(num_internships=Count('internship'))#.order_by('-num_internships')


class State(models.Model):
    " Brazilian State "
    
    name = models.CharField(u'Nome', max_length=180)
    uf = models.CharField(u'UF', max_length=2)
    
    objects = PassThroughManager.for_queryset_class(StateQuerySet)()

    class Meta:
        verbose_name='Estado'
        app_label = 'address'
        
    __unicode__ = lambda x: x.uf

