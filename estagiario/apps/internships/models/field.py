# -*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField


class Field(models.Model):
    name    = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    __unicode__ = lambda x: x.name

    class Meta:
        verbose_name='Área'
        app_label='internships'