# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Internship

class InternshipForm(ModelForm):
    class Meta:
        model = Internship
        exclude = ('slug', 'created', 'modified')
