# -*- coding: utf-8 -*-


"""
    - url keyword params:
        - field-slug
        - state
    - get params
        - ...

    - get ordering

    - return results 


    - salvar filtro
    


"""

from internships.filters import TagFilter, WeekHoursFilter, StateSelector, CityFilter,CompanySizeFilter, FieldFilter
from internships.models import Internship
class InternshipSearch(object):
    def __init__(self, request, **kwargs):
        self.request = request        
        self.qset = Internship.objects.available()

        field_slug = kwargs.get('field_slug', None)
        self.field_filter   = FieldFilter(request, field_slug=field_slug)
        
        state_uf = kwargs.get('state_uf', None)
        self.state_filter   = StateSelector(request, state_uf=state_uf)
        
        self.city_filter    = CityFilter(request)
        self.city_filter.set_state( self.state_filter.get_state )

        self.tag_filter     = TagFilter(request)
        self.hours_filter   = WeekHoursFilter(request)
        self.size_filter    = CompanySizeFilter(request)
        

    def _apply_filters(self):
        qset = self.qset
        qset = self.field_filter.parse_query(qset)
        qset = self.state_filter.parse_query(qset)
        qset = self.city_filter.parse_query(qset)
        qset = self.tag_filter.parse_query(qset)
        qset = self.hours_filter.parse_query(qset)
        qset = self.size_filter.parse_query(qset)
        return qset

    def _order_by(self):
        pass

    def get_queryset(self):
        qset = self._apply_filters()
        #self._order_by()
        return qset



