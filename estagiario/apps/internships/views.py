# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import redirect
from annoying.decorators import render_to
from forms import InternshipForm
from address.models import State
from internships.models import Internship
from taggit.models import Tag


# def get_ordered_tags():
#     sorted_tags = []
#     for t in Tag.objects.all():
#         tag_dic = {}
#         tag_dic[t] = Internship.objects.filter(tag=t).count()
#         tags_list.append(tag_dic)

#     sorted_tags = sorted(sorted_tags, key=lambda x: x.values()[0])     
#     return sorted_tags



# class StateOption(object):
#     ACTIVE_CLASS = 'active'
#     GET_PARAM = 'uf'
#     def __init__(self, obj, is_active):
#         self.obj = obj
#         self.label = obj.name
#         self.val = obj.uf
#         self.is_active = is_active

    
#     def active_class(self):
#         return self.ACTIVE_CLASS if self.is_active else ''


# class StateFilter2(object):
#     GET_PARAM = 'uf'

#     def __init__(self, request):
#         self.request = request
        
#         val = request.GET.get('uf', None)
#         self.val = val.lower() if val is not None else ''

#     def parse_queryset(self, qset):
#         if self.val is None: return qset        
#         return qset.filter(state__uf=self.val.lower())
        
#     def _options(self, hot=False, public=True):        
#         qstates = State.objects.all()
#         if public:
#             active_states = Internship.objects.available().values_list('state__id', flat=True).distinct()
#             qstates = qstates.filter(id__in=active_states)

#         if hot:
#             return qstates[:settings.ANON_RESULTS_COUNT]
        
#         return qstates
    
#     def _parse_options(self, objs):
#         options = []
#         for obj in objs:
#             is_active = obj.uf.lower() == self.val
#             sto = StateOption(obj, is_active)
#             options.append(sto)
#         return options
    
#     def options(self):
#         return self._parse_options(self._options())
from filters import TagFilter, WeekHoursFilter, StateSelector


@render_to('index.html')
def list_internships(request, state_uf=None, field_slug=None):
    """
    List/Search internships available
    + results are limited to <settings.ANON_RESULTS_COUNT> for anonymous users
    
    - Filter:
        - state 
        - city 
        - area 
        - company_size
        - tags
        - weekly hours
        - semester
    
    - Order:
        - relevance
        - salary
        - dt_created
    """
    results = Internship.objects.all()
    
    #path_prefix = request.path.split('/')[1]
    #uf = None
    #if len(path_prefix) == 2:
    #    uf = path_prefix
    
    state_selector = StateSelector(request, state_uf)
    results = state_selector.parse_query(results)
    
    tag_filter = TagFilter(request)
    results = tag_filter.parse_query(results)

    hours_filter = WeekHoursFilter(request)
    results = hours_filter.parse_query(results)
    
    print hours_filter.get_options()

    #ins = state_filter.parse_queryset(ins)
    return locals()


@render_to('index.html')
def show_internship(request, state_uf=None, ins_slug=None):
    """ auto_now_add=    """
    return locals()


@render_to('add_internship.html')
def add_internship(request):
    "Publishes a new internship opening"
    form = InternshipForm(request.POST or None)
    #print form.as_ul()
    #print form

    if form.is_valid():
        ins = form.save()
        return redirect(ins)
        
    return locals()
