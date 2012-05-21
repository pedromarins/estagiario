# -*- coding: utf-8 -*-
from base_filter import BaseFilter, FilterOption
from taggit.models import Tag
from internships.models import Internship

class TagFilter(BaseFilter):
    class Meta:
        get_param = 'tags'
        default_css = []
        active_css = 'active'
        clear_option = 'Todas'

    def _list_items(self):
        "data used to be filtered"
        count_tag = lambda x: Internship.objects.by_tag(x).count()
        return [{ x: count_tag(x)} for x in Tag.objects.all() ]

    
    def _make_option(self, data):
        "option obj"
        obj, order = data.items()[0]
        label = obj.name
        val = obj.name.lower()
        is_active = self.val == val
        return FilterOption(obj, label, val, is_active, order)
    
    def _list_options(self, enabled=True):
        "options"
        opts = []
        for obj in self._list_items():
            opts.append(self._make_option(obj))
        return opts
    def _order_options(self, lst):
        return sorted(lst, key=lambda x: x.order, reverse=True)
    
    def parse_query(self, qset):
        if not bool(self.val):
            return qset
        return qset.filter(tags__in=Tag.objects.filter(name=self.val))

