# -*- coding: utf-8 -*-
import factory
from base_factory import BaseFactory
from internships.models import Field, Internship
from internships.models.internship import NEGOTIABLE_CHOICES
from datetime import date, timedelta
import random
from address.models import State, City

from default_values import FIELD_DEFAULTS, COMPANIES, ADDRESSES

## internship.Field ##
class FieldFactory(factory.Factory):
    FACTORY_FOR = Field
    
    @classmethod 
    def make_for_test(cls):        
        return [ cls(name=name) for name in FIELD_DEFAULTS ]



"""     internship.Internship      """

## Helpers
random_negotiable = lambda a: random.choice(NEGOTIABLE_CHOICES._choice_dict.values())
random_field = lambda a: random.choice( list(Field.objects.all()) )

ROLES = ['programador', 'designer', 'ilustrador', 'digitador', ]
random_role = lambda a: random.choice(ROLES)

## Factory
class InternshipFactory(factory.Factory):
    FACTORY_FOR = Internship

    field   = factory.LazyAttribute(random_field)
    role    = factory.LazyAttribute(random_role)

    description = 5 * 'Lorem Ipsum is simply dummy text of the printing and typesetting \n'
    
    weekly_hours = factory.LazyAttribute(lambda a: random.choice([20, 25, 30]))
    
    relevance   = -1
    featured    = False
    approved    = True 
    active      = True
    expiration  = factory.LazyAttribute(lambda x: date.today() + timedelta(days=30))
    
    min_semester = 0

    transport       = factory.LazyAttribute(random_negotiable)
    health          = factory.LazyAttribute(random_negotiable)
    food            = factory.LazyAttribute(random_negotiable)
    flexible_hours  = factory.LazyAttribute(random_negotiable)

    city = factory.LazyAttribute(lambda a: City.objects.all()[0] )
    state = factory.LazyAttribute(lambda a: a.city.state )
    street = 'Rua de exemplo'
    number = '10'
    district = 'Bairro'
    cep = '24123010'



def fill_company(ins, company, **kwargs):
    data = COMPANIES[company]
    for k,v in kwargs:
        data[k] = v
    ins.company_name    = data['name']
    ins.company_url     = data['url']
    ins.company_img     = 'company_logos/' + data['img']
    ins.company_size    = data['size']
    return ins

def fill_address(ins, addr):
    data = ADDRESSES[addr]
    state = State.objects.get(uf=data['state'])
    city = City.objects.filter(state=state).filter(name__iexact=data['city'])[0]

    ins.street = data['street']
    ins.number = data['number']
    #ins.complement = data['complement']
    ins.district = data['district']
    ins.cep = data['cep']
    
    ins.city = city
    ins.state = state
    return ins

def fill_tags(ins, *args):
    for tag in args:
        ins.tags.add(tag)
    return ins