# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Count
from django.db.models.query import QuerySet

from model_utils.managers import PassThroughManager
from django.db.models import get_model

class CityQuerySet(QuerySet):
    def _cities_with_internships_ids(self):
        return get_model('internships', 'Internship').objects.available().values_list('city__id', flat=True).distinct()
    
    def has_internship(self):
        "cities with available internships ordered by descending internship count"
        active_states = self._cities_with_internships_ids()
        return self.filter(id__in=active_states).annotate(num_internships=Count('internship'))#.order_by('-num_internships')



class City(models.Model):
    " Brazilian City "
    name = models.CharField(u'Nome', max_length=180)
    state = models.ForeignKey('address.State')
    
    objects = PassThroughManager.for_queryset_class(CityQuerySet)()
    
    class Meta:
        verbose_name='Cidade'
        app_label = 'address'

    def __unicode__(self):
        return u'%s [%s]' % (self.name, self.state.uf.upper())

