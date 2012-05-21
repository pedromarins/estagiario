# -*- coding: utf-8 -*-
from base_filter import BaseFilter, FilterOption
from internships.models import Internship

class CompanySizeFilter(BaseFilter):
    class Meta:
        get_param = 'porte'
        default_css = []
        active_css = 'active'
        clear_option = 'Todas'

    def _list_items(self):
        "data used to be filtered"
        return [(sz[0], sz[2]) for sz in Internship.COMPANY_SIZES._full]
    
    def _make_option(self, data):
        "option obj"
        obj = data
        order = data[0]
        label = data[1]
        val = data[0]
        is_active = self.val == val
        return FilterOption(obj, label, val, is_active, order)
    
    def _list_options(self, enabled=True):
        "options"
        opts = []
        for obj in self._list_items():
            opts.append(self._make_option(obj))
        return opts
    
    def _order_options(self, lst):
        return lst
    
    def parse_query(self, qset):
        if not bool(self.val): 
            return qset
        return qset.filter(company_size=self.val)