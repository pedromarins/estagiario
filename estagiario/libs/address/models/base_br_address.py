# -*- coding: utf-8 -*-
from django.db import models

class BRAddressModel(models.Model): 
    street          = models.CharField(u'Rua',          max_length=180)
    number          = models.CharField(u'Número',       max_length=60)
    complement      = models.CharField(u'Complemento',  max_length=180, blank=True,null=True)
    district        = models.CharField(u'Bairro',       max_length=180, blank=True,null=True)

    city            = models.ForeignKey('address.City', verbose_name='Cidade')
    state           = models.ForeignKey('address.State',verbose_name='Estado')

    cep             = models.CharField(u'CEP',  max_length=10)
    
    class Meta:
        abstract = True