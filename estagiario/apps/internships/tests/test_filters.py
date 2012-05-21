# -*- coding: utf-8 -*-
from django.test import TestCase

from django.test.client import RequestFactory

from datetime import date, timedelta
import factory
from factories.shortcuts import create_internship, setup_fields, setup_states

from internships.models import Internship, Field
from internships.filters import InternshipSearch
factory.Factory.default_strategy = factory.CREATE_STRATEGY if True else factory.BUILD_STRATEGY
from address.models import State

def add_date_shortcuts(obj):
    setattr(obj, 'today', date.today())
    setattr(obj, 'tomorow', date.today() + timedelta(days=1))
    setattr(obj, 'yesterday', date.today() - timedelta(days=1))
    return obj

class TestInternshipFilter(TestCase):
    fixtures = ['state', 'city', 'field']

    def setUp(self):
        add_date_shortcuts(self)
        self.factory = RequestFactory()

    def tearDown(self):
        Internship.objects.all().delete()
    
    def _get(self, url):
        'factory GET for url'
        return self.factory.get(url)
    
    def test_no_filter(self):
        " all available internships if there's no filter "
        request = self.factory.get('/estagios/')    
        
        create_internship('sparkit', 'sg')        
        # expired > not available
        create_internship('sparkit', 'rio', tags=['tag1', 'tag2'], expiration=self.yesterday)

        search = InternshipSearch(request)
    
        self.assertEquals(len(search.get_queryset()), 1)
    
    def test_state_get_filter(self):
        ''' filter state using GET: ?uf=RJ '''
        request = self.factory.get('/estagios/?uf=rj')

        i1 = create_internship('visagio', 'rio', tags=['tag3', ])
        i2 = create_internship('vale', 'sampa', tags=['tag1',])
        
        int_search = InternshipSearch(request)
        results = int_search.get_queryset()

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0], i1)



    def test_state_url_filter(self):
        ''' filter state using GET: ?uf=RJ '''
        request = self.factory.get('/estagios/')

        i1 = create_internship('visagio', 'rio', tags=['tag3', ])
        i2 = create_internship('vale', 'sampa', tags=['tag1',])
        
        int_search = InternshipSearch(request, state_uf='sp')
        results = int_search.get_queryset()

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0], i2)

        request = self.factory.get('/estagios/')
        int_search = InternshipSearch(request, state_uf='ac')
        results = int_search.get_queryset()
        self.assertEquals(len(results), 0)

    def test_field_filter(self):
        request = self.factory.get('/direito/')
        direito = Field.objects.get(slug='direito')

        i1 = create_internship('visagio', 'rio', tags=['tag3', ], field=direito)
        i2 = create_internship('vale', 'sampa', tags=['tag1',])

        
        int_search = InternshipSearch(request, field_slug=direito.slug)
        results = int_search.get_queryset()

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0], i1)

    def test_tag_filter(self):
        "filter by tags"
        i1 = create_internship('sparkit', 'sg')        
        i2 = create_internship('vale', 'sampa', tags=['tag1',])
        i3 = create_internship('visagio', 'rio', tags=['tag1', 'tag3', ])

        search = InternshipSearch(self._get('/estagios/?tags=tag9'))
        self.assertEquals(len(search.get_queryset()), 0)

        search = InternshipSearch(self._get('/estagios/?tags=tag1'))
        self.assertEquals(len(search.get_queryset()), 2)


        search = InternshipSearch(self._get('/estagios/?tags=tag3'))
        self.assertEquals(search.get_queryset()[0], i3)


        #search = InternshipSearch( self._get('/estagios/?tags=tag9') )
        #print search.get_queryset()
        #self.assertEquals(0, search.get_queryset().count())
        
        



        #tag_filter = TagFilter(request)
        #results = tag_filter.parse_query(results)




    # url(r'^(?P<field_slug>\w){6,13}/(?P<state_uf>\w{2})/$', 'list_internships'),
    # url(r'^estagios/(?P<state_uf>\w{2})/$', 'list_internships'),

        
