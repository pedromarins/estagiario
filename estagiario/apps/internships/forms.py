# -*- coding: utf-8 -*-
#from django.forms import ModelForm
from models import Internship

import floppyforms as forms


# class DatePicker(forms.DateInput):
#     template_name = 'datepicker.html'

#     class Media:
#         js = (
#             'js/jquery.min.js',
#             'js/jquery-ui.min.js',
#         )
#         css = {
#             'all': (
#                 'css/jquery-ui.css',
#             )
#         }


# class DateForm(forms.Form):
#     date = forms.DateField(widget=DatePicker)
    
class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = (
            'role', 'field', 'description', 
            'company_name', 'company_url', 'company_img', 'company_size',
            'weekly_hours', 'salary', 'min_semester',
            'transport','health','food','flexible_hours',    
            'expiration',
            'street','number','complement', 'district', 'cep',
            'state', 'city',
            'tags'
        )
    #           = models.CharField(u'Rua',          max_length=180)
    #           = models.CharField(u'Número',       max_length=60)
    #       = models.CharField(u'Complemento',  max_length=180, blank=True,null=True)
    #         = models.CharField(u'Bairro',       max_length=180, blank=True,null=True)

    #             = models.ForeignKey('address.City', verbose_name='Cidade')
    #            = models.ForeignKey('address.State',verbose_name='Estado')

    # cep             = models.CharField(u'CEP',  max_length=10)
    


    
    # #            = models.ForeignKey('internships.Field')
    # # slug            = models.SlugField(blank=True)

    # #     = models.CharField('Empresa', max_length=64)
    # #      = models.URLField('Site')
    # #      = models.ImageField('Logo', upload_to='company_logos', null=True)
    # #     = models.CharField(choices=COMPANY_SIZES, default=COMPANY_SIZES.peq, max_length=5)

    # #     = models.PositiveSmallIntegerField('Carga horária', choices=[(20,'20'), (25, '25'), (30, '30')])
    # #           = models.DecimalField('Salário', max_digits=7, decimal_places=2, null=True)
    # #     = models.PositiveSmallIntegerField(default=0)

    # #        = models.IntegerField('Vale Transporte',  default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)


    # # # relevance index
    # # relevance       = models.IntegerField(default=-1)
    # # # Paid for top positions
    # # featured        = models.IntegerField(blank=True) 
    # # # Date internship will be removed from public site
    # #       = models.DateField('Data de expiração')

    # # approved = models.BooleanField()
    # # active = models.BooleanField(default=True)