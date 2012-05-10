# -*- coding: utf-8 -*-

from django.contrib import admin
from internships.models import Internship

class InternshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Internship, InternshipAdmin)