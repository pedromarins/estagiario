# -*- coding: utf-8 -*-
import factory
from factories import StateFactory, FieldFactory, InternshipFactory, fill_company, fill_address, fill_tags

factory.Factory.default_strategy = factory.CREATE_STRATEGY

def create_internship(company_key, address_key, **kwargs):
    ins = InternshipFactory.build()
    fill_company(ins, company_key)
    fill_address(ins, address_key)
    ins.save()
    ins = fill_tags(ins, *kwargs.get('tags',[]) )
    return ins

def run():
    StateFactory.make_for_test()
    FieldFactory.make_for_test()


    create_internship('sparkit', 'rio', tags=['tag1', 'tag2'])
    create_internship('sparkit', 'sg')
    
    create_internship('visagio', 'rio', tags=['tag3', ])
    
    create_internship('vale', 'sampa', tags=['tag1',])