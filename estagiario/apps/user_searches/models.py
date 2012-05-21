# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices

NOTIFICATION_CHOICES = Choices(
    (-1, 'none',            u'none'), 
    ( 0, 'disabled',        u'Desabilitada'), 
    ( 1, 'email_day',       u'Email Diário'),
    ( 2, 'email_week',      u'Email Semanal'),

)

class UserSearch(TimeStampedModel):
    label           = models.CharField(max_length=128)
    dt_notified     = models.DateTimeField(null=True)
    
    method          = models.IntegerField('Tipo de notificação',  default=NOTIFICATION_CHOICES.email_day, choices=NOTIFICATION_CHOICES)
    
    city            = models.ForeignKey('address.City', verbose_name='Cidade', null=True)
    state           = models.ForeignKey('address.State',verbose_name='Estado', null=True)
    
    tags            = models.CommaSeparatedIntegerField(max_length=128, blank=True, null=True) 
    field           = models.ForeignKey('internships.Field')

    weekly_hours    = models.PositiveSmallIntegerField('Carga horária', choices=[(20,'20'), (25, '25'), (30, '30')], null=True)
    min_semester    = models.PositiveSmallIntegerField(default=0, null=True)

    # transport       = models.IntegerField('Vale Transporte',  default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # health          = models.IntegerField('Plano de saúde',   default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # food            = models.IntegerField('Vale Alimentação', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # flexible_hours  = models.IntegerField('Horário Flexível', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)


class UserNotification(TimeStampedModel):
    label           = models.CharField(max_length=128)
