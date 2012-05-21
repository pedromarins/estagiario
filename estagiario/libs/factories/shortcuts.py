# -*- coding: utf-8 -*-
from address_factory import STATES, StateFactory
from internship_factory import InternshipFactory, FieldFactory, fill_address, fill_company, fill_tags

def setup_fields():
    FieldFactory.make_for_test()

def setup_states(*args):
    if not(args):
        args = STATES.keys()
    
    for uf in args:
        name = STATES[uf]['name']
        cities = STATES[uf]['cities']
        StateFactory.make_with_cities(name, uf, cities, save=True)

def create_internship(company_key, address_key, **kwargs):
    tag_list = kwargs.pop('tags',[])

    ins = InternshipFactory.build()
    fill_company(ins, company_key)
    fill_address(ins, address_key)
    
    [ setattr(ins, k, v) for k,v in kwargs.items() ]

    ins.save()

    ins = fill_tags(ins, *tag_list )
    
    return ins