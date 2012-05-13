# -*- coding: utf-8 -*-
from taggit.models import Tag
from internships.models import Internship

class FilterOption(object):
    def __init__(self, obj, label, val, is_active, order=0, active_class='active'):
        self.obj = obj
        self.is_active = is_active
        self.label = label
        self.val = val
        self.order = order
        self.active_class = active_class if self.is_active else ''


class BaseFilter(object):
    class Meta:
        get_param = 'q'
        default_css = []
        active_css = 'active'
        clear_option = 'Todos'
    
    def __init__(self, request):
        """
            - listar opções
            - listar opções principais 
            - get_param 
            - gerar val da query 
            - parsear queryse 
            - gerar opcões
            - saber se opção é ativa
            - todos
        """
        self.request = request
        self.val = self.request.GET.get(self.Meta.get_param, None)
    
    
    def _list_items(self):
        "data used to be filtered"
        return []
    
    def _make_option(self, **kws):
        "option obj"
        return FilterOption(**kws)
    
    def _list_options(self, enabled=True):
        "options"
        opts = []
        for obj in self._list_items():
            opts.append(self._make_option(obj))
        return opts


    def _order_options(self, lst):
        return lst
            
    def _add_clear_option(self, lst):
        is_active = not bool(self.val)
        return [ FilterOption(obj=None, label=self.Meta.clear_option, val='', is_active=is_active, order=-1), ] + lst
    
    def get_options(self, limit=None):
        options = self._list_options(enabled=True)        
        options = self._order_options(options)
        options = self._add_clear_option(options)

        if limit is None:
            return options
        else:
            return options[:limit+1]            


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


class WeekHoursFilter(BaseFilter):
    class Meta:
        get_param = 'horas'
        default_css = []
        active_css = 'active'
        clear_option = 'Todas'

    def _list_items(self):
        "data used to be filtered"
        return [('20','20'), ('25', '25'), ('30', '30')]

    
    def _make_option(self, data):
        "option obj"
        obj = data[0]
        order = int(data[0])
        label = data[0]
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
        return qset.filter(weekly_hours=self.val)



from django.forms.widgets import Select
from address.models import State
class StateSelector(object):
    def __init__(self, request, state_uf=None):
        self.request = request        
        options = State.objects.has_internship().values_list('uf', 'name')
        self.options = [('', 'Todos'),] + list(options)

        uf = request.GET.get('uf', None)
        if state_uf is not None:
            uf = state_uf.lower()
        self.val = uf
    
    def parse_query(self, qset):
        if self.val:
            qset.filter(state__uf=self.val.lower())
        return qset
            
    
    def render(self):
        se = Select(choices=self.options)
        name = 'state-select'
        return se.render(name, self.val, attrs={'id':name})


# company_size

#  COMPANY_SIZES = Choices(
#         ('peq',     'Pequeno Porte'), 
#         ('med',     u'Médio Porte'),
#         ('grd',     'Grande Porte'),
#     )
      


# class TagFilter(BaseFilter):
#     class Meta:
#         get_param = 'tags'
#         default_css = []
#         active_css = 'active'

#     class Ordering:
#         order_key = lambda x: x.order
#         order_reverse = True    
    
#     def _list_items(self):
#         "data used to be filtered"
#         count_tag = lambda x: Internship.objects.by_tag(x).count()
#         return [{ x: count_tag(x)} for x in Tag.objects.all() ]

    
#     def _make_option(self, data):
#         "option obj"
#         obj, order = data.items()[0]
#         label = obj.name
#         val = obj.name.lower()
#         is_active = self.val == val
#         return FilterOption(obj, label, val, is_active, order)
    
#     def _list_options(self, enabled=True):
#         "options"
#         opts = []
#         for obj in self._list_items():
#             opts.append(self._make_option(obj))
#         return opts
#     def _order_options(self, lst):
#         return sorted(lst, key=lambda x: x.order, reverse=True)
    
#     def parse_query(self, qset):
#         if self.val is None: return qset
#         return qset.filter(tags=val)
