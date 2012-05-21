# -*- coding: utf-8 -*-
from base_filter import BaseFilter, FilterOption


from django.forms.widgets import Select
from address.models import State
class StateSelector(object):
    def __init__(self, request, state_uf=None):
        self.request = request        
        options = State.objects.has_internship().values_list('uf', 'name')
        self.options = [('estagios', 'Estados'),] + list(options)

        uf = request.GET.get('uf', None)
        if state_uf is not None:
            uf = state_uf.lower()
        self.val = uf if uf is None else uf.lower() 
    
    def get_state(self):
        if self.val:
            states = State.objects.filter(uf=self.val)
            if len(states): 
                return states[0]
        return None

    def parse_query(self, qset):
        if self.val:
            return qset.filter(state__uf=self.val)
        return qset
            
    
    def render(self):
        se = Select(choices=self.options)
        name = 'stateselect'
        return se.render('stateselect', self.val, attrs={'id':'id-state-select'})


