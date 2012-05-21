# -*- coding: utf-8 -*-
import factory
from base_factory import BaseFactory
from address.models import State, City


STATES = {
    'rj': {  'name': 'Rio de Janeiro', 'uf': 'rj',
            'cities': ['Rio de Janeiro', 'São Gonçalo', 'Niterói'], },

    'sp': {  'name': 'São Paulo', 'uf': 'sp',
            'cities': ['São Paulo', 'Guarulhos', 'Campinas', 'São Bernardo do Campo'], },

    'mg': {  'name': 'Minas Gerais', 'uf': 'mg',
            'cities': ['Belo Horizonte', 'Uberlândia', 'Contagem', 'Juiz de Fora'], },
}

class CityFactory(factory.Factory):
    FACTORY_FOR = City


class StateFactory(factory.Factory):
    FACTORY_FOR = State
    
    @classmethod
    def make_with_cities(cls, name, uf, city_names=[], save=False):
        #state = cls._make(save, name=name, uf=uf)
        #cities = [CityFactory._make(save, state=state, name=c) for c in city_names]
        state = cls(name=name, uf=uf)        
        cities = [CityFactory(state=state, name=c) for c in city_names]
        return state, cities

    @classmethod 
    def make_for_test(cls, save=True):
        for uf, st in STATES.items():
            cls.make_with_cities(st['name'], uf, st['cities'], save=save)        