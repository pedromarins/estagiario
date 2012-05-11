# -*- coding: utf-8 -*-
from django.contrib import admin
from internships.models import Internship, Field


class InternshipAdmin(admin.ModelAdmin):
    pass


class FieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(Internship, InternshipAdmin)
admin.site.register(Field, FieldAdmin)