# -*- coding: utf-8 -*-
from base_filter import BaseFilter, FilterOption
from address.models import State, City

class CityFilter(BaseFilter):
    class Meta:
        get_param = 'cidade'
        default_css = []
        active_css = 'active'
        clear_option = 'Todas'
    
    def set_state(self, state):
        setattr(self, 'state', state)

    def _list_items(self):
        "data used to be filtered"
        if not self.state:
            return []
        return list(City.objects.filter(state=self.state).has_internship())

    def _make_option(self, data):
        "option obj"
        order = data.num_internships
        val = str(data.id)
        is_active = self.val == val
        return FilterOption(data, data.name, val=val, is_active=is_active, order=order)
    
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
        return qset.filter(city__id=self.val)