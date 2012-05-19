# -*- coding: utf-8 -*-
import re
from django.utils.safestring import mark_safe
from django.conf import settings
from django import template
register = template.Library()



@register.simple_tag
def active_field(request, pattern):
    path = request.path.lower()
    if path.count(pattern):
        return settings.CSS.get('field_menu_active', 'active')
    return ''