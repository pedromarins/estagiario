# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Internship(TimeStampedModel):
    COMPANY_SIZES = Choices(
        ('peq',     'Pequeno Porte'), 
        ('med',     'Médio Porte'),
        ('grd',     'Grande Porte'),
    )

    role            = models.CharField('Cargo', max_length=64)
    field           = models.ForeignKey('internships.Field')
    description     = models.TextField('Descrição')
    tags            = TaggableManager()
    slug            = models.SlugField(blank=True)

    company_name    = models.CharField('Empresa', max_length=64)
    company_url     = models.URLField('Site')
    company_img     = models.ImageField('Logo', upload_to='company_logos', null=True)
    company_size    = models.CharField(choices=COMPANY_SIZES, default=COMPANY_SIZES.peq, max_length=5)

    weekly_hours    = models.PositiveSmallIntegerField('Carga horária', choices=[(20,'20'), (25, '25'), (30, '30')])
    salary          = models.DecimalField('Salário', max_digits=7, decimal_places=2, null=True)

    expiration      = models.DateField('Data de expiração')
    
    
    district        = models.CharField(u'Bairro',max_length=180)
    cep             = models.CharField(u'CEP',max_length=180)
    street          = models.CharField(u'Rua',max_length=180)
    number          = models.CharField(u'Número',max_length=60)
    complement      = models.CharField(u'Complemento',max_length=180, blank=True,null=True)

    city            = models.ForeignKey('address.City')
    state           = models.ForeignKey('address.State')


    #período
    #temporário

    class Meta:
        verbose_name='Vaga'
        app_label='internships'