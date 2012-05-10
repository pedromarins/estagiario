# -*- coding: utf-8 -*-

from django.db import models

class Internship(models.Model):
    role            = models.CharField('Cargo', max_length=64)
    #field           = models.ChoiceField()
    description     = models.TextField('Descrição')


    company_name    = models.CharField('Empresa', max_length=64)
    company_url     = models.URLField('Site')
    company_img     = models.ImageField('Logo', null=True)
    #company_size = models.ChoiceField()

    #created
    #expires
    #weekly_hours = models.PositiveSmallIntegerField('Carga horária', choices=[(4,4), (6,6)])
    salary = models.DecimalField('Salário', max_digits=7, decimal_places=2, null=True)
    #período
    #temporário



    class Meta:
        verbose_name='Vaga'
        app_label='internships'
