# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager
from address.models import BRAddressModel
from internship_queryset import InternShipQuerySet
from model_utils.managers import PassThroughManager

NEGOTIABLE_CHOICES = Choices(
    (-1, 'not_informed',    u'Não informar'), 
    ( 0, 'no',              u'Não'), 
    ( 1, 'negotiable',      u'A negociar'),
    ( 2, 'yes',             u'Sim'),
)

class Internship(TimeStampedModel, BRAddressModel):
    COMPANY_SIZES = Choices(
        ('peq',     'Pequeno Porte'), 
        ('med',     u'Médio Porte'),
        ('grd',     'Grande Porte'),
    )

    role            = models.CharField('Cargo', max_length=64)
    field           = models.ForeignKey('internships.Field')
    description     = models.TextField('Descrição')
    slug            = models.SlugField(blank=True)
    tags            = TaggableManager()

    company_name    = models.CharField('Empresa', max_length=64)
    company_url     = models.URLField('Site', blank=True)
    company_img     = models.ImageField('Logo', upload_to='company_logos', null=True)
    company_size    = models.CharField(choices=COMPANY_SIZES, default=COMPANY_SIZES.peq, max_length=5)

    weekly_hours    = models.PositiveSmallIntegerField('Carga horária', choices=[(20,'20'), (25, '25'), (30, '30')])
    salary          = models.DecimalField('Salário', max_digits=7, decimal_places=2, null=True)
    min_semester    = models.PositiveSmallIntegerField(default=0)

    transport       = models.IntegerField('Vale Transporte',  default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    health          = models.IntegerField('Plano de saúde',   default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    food            = models.IntegerField('Vale Alimentação', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    flexible_hours  = models.IntegerField('Horário Flexível', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    

    # relevance index
    relevance       = models.IntegerField(default=-1)
    # Paid for top positions
    featured        = models.BooleanField(default=False) 
    # Date internship will be removed from public site
    expiration      = models.DateField('Data de expiração')

    
    approved = models.BooleanField() # if False, should never be displayed
    active = models.BooleanField(default=True)

    objects = PassThroughManager.for_queryset_class(InternShipQuerySet)()

    def __unicode__(self):
        return self.role + ' na ' + self.company_name
    
    class Meta:
        verbose_name='Vaga'
        app_label='internships'