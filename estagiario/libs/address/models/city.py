# -*- coding: utf-8 -*-
from django.db import models

class City(models.Model):
    " Brazilian City "
    name = models.CharField(u'Nome', max_length=180)
    state = models.ForeignKey('address.State')
    
    class Meta:
        verbose_name='Cidade'
        app_label = 'address'

    def __unicode__(self):
        return u'%s [%s]' % (self.name, self.state.uf.upper())