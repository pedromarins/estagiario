# -*- coding: utf-8 -*-
import factory
from datetime import timedelta
from internships.models import Internship, Field
from address.models import State, City


## address ##
class CityFactory(factory.Factory):
    FACTORY_FOR = City

class StateFactory(factory.Factory):
    FACTORY_FOR = State
    @classmethod
    def create_with_cities(cls, name, uf, city_names=[]):
        st = cls(name=name, uf=uf)
        if not city_names:
            return st            
        return st, [ CityFactory(name=x, state=st) for x in city_names ]



## internships ##
ROLES = ['programador', 'designer', 'ilustrador', 'digitador', ]

class FieldFactory(factory.Factory):
    FACTORY_FOR = Field
    name = 'Field'

class InternshipFactory(factory.Factory):
    FACTORY_FOR = Internship
    
    field   = factory.LazyAttribute(lambda a: FieldFactory())
    role    = factory.LazyAttribute(lambda a: random.choice(ROLES))

    description = 5 * 'Lorem Ipsum is simply dummy text of the printing and typesetting \n'
    
    weekly_hours = factory.LazyAttribute(lambda a: random.choice([20, 25, 30]))
    
    relevance   = -1
    featured    = None
    expiration  = factory.LazyAttribute(lambda x: x + timedelta(days=30))
    
    #salary
    min_semester = 0
    # company_name    = models.CharField('Empresa', max_length=64)
    # company_url     = models.URLField('Site')
    # company_img     = models.ImageField('Logo', upload_to='company_logos', null=True)
    # company_size    = models.CharField(choices=COMPANY_SIZES, default=COMPANY_SIZES.peq, max_length=5)
    # transport       = models.IntegerField('Vale Transporte',  default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # health          = models.IntegerField('Plano de saúde',   default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # food            = models.IntegerField('Vale Alimentação', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)
    # flexible_hours  = models.IntegerField('Horário Flexível', default=NEGOTIABLE_CHOICES.not_informed, choices=NEGOTIABLE_CHOICES)





# def create_models_for_address():


# def run():
#     sg      = City.objects.get(name='São Gonçalo')
#     rio     = City.objects.get(name='Rio de Janeiro')
#     sampa   = City.objects.get(name='São Paulo')
#     bh      = City.objects.get(name='Belo Horizonte')
#     recife  = City.objects.get(name='Recife') #PE


#     # Returns a User instance that's not saved
# user = UserFactory.build()

# # Returns a saved User instance
# user = UserFactory.create()


# # Same as UserFactory.create()
# user = UserFactory()
#     