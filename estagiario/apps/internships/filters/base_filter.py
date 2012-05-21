# -*- coding: utf-8 -*-

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
