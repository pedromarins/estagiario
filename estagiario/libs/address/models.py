# -*- coding: utf-8 -*-
from django.db import models

class State(models.Model):
    "Defines a state"
    name = models.CharField(u'Nome', max_length=180)
    uf = models.CharField(u'UF', max_length=2)
    
    class Meta:
        verbose_name='Estado'
        verbose_name_plural = 'Cadastro de Estados'
        
    __unicode__ = lambda x: x.name
    
class City(models.Model):
    "Defines a city"
    name = models.CharField(u'Nome', max_length=180)
    state = models.ForeignKey(State)
    
    class Meta:
        verbose_name='Cidade'
        verbose_name_plural = 'Cadastro de Cidades'

    __unicode__ = lambda x: x.name