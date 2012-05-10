# -*- coding: utf-8 -*-
from django.contrib import admin
from models import City, State

admin.site.register(State, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)    