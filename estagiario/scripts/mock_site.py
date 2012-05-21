# -*- coding: utf-8 -*-
import factory
from factories import StateFactory, FieldFactory, create_internship

factory.Factory.default_strategy = factory.CREATE_STRATEGY


def run():
    StateFactory.make_for_test()
    FieldFactory.make_for_test()


    create_internship('sparkit', 'rio', tags=['tag1', 'tag2'])
    create_internship('sparkit', 'sg')
    
    create_internship('visagio', 'rio', tags=['tag3', ])
    
    create_internship('vale', 'sampa', tags=['tag1',])