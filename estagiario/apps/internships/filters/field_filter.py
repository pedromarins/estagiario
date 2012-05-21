# -*- coding: utf-8 -*-
from base_filter import FilterOption
from internships.models import Field

class FieldFilter(object):
    
    class Meta:
        active_css = 'active'
    
    def __init__(self, request, field_slug=None):
        self.request = request
        self.field_slug = field_slug
        self._options = []
    
    
    def _add_option(self, field):
        "append obj as FilterOption to _options list"
        is_active = self.field_slug == field.slug
        opt = FilterOption(field, field.name, field.slug, is_active, field.id)
        self._options.append(opt)
    
    def get_options(self):
        "list options"
        if not len(self._options):
            [ self._add_option(fd) for fd in Field.objects.all() ]
        return self._options    

    def parse_query(self, qset):
        if self.field_slug:
            qset = qset.filter(field__slug__iexact=self.field_slug)
        return qset