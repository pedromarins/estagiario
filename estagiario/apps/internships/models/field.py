# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices


class Field(models.Model):
    name    = models.CharField(max_length=64)
    class Meta:
        verbose_name='Área'
        app_label='internships'