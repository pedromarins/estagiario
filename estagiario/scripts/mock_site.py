# -*- coding: utf-8 -*-
from address.models import City, State
from factories import InternshipFactory, StateFactory

RJ_CITIES = ['Rio de Janeiro', 'São Gonçalo', 'Niterói']
SP_CITIES = ['São Paulo', 'Guarulhos', 'Campinas', 'São Bernardo do Campo']
MG_CITIES = ['Belo Horizonte', 'Uberlândia', 'Contagem', 'Juiz de Fora']
PE_CITIES = ['Recife',]


def _create_state(uf, name, city_names):
    return list(StateFactory.create_with_cities(name, uf, city_names=city_names))

def create_address():
    states = {}        
    states['rj'] = _create_state('rj', 'Rio de Janeiro', RJ_CITIES)
    states['sp'] = _create_state('sp', 'São Paulo', SP_CITIES)
    states['mg'] = _create_state('mg', 'Minas Gerais', MG_CITIES)
    states['pe'] = _create_state('pe', 'Pernambuco', PE_CITIES)
    return states
    
#company_logos/medium_sparkit-19055_1.jpg
#company_img: company_logos/medium_sparkit-19055_1.jpg,
def run():
    sd = create_address()


- fields: {active: true, approved: true, cep: 24470-060, city: 2258, company_img: ,
    company_name: SparkIT, company_size: peq, company_url: 'http://sparkit.com.br/',
    complement: Sobrado, created: !!timestamp '2012-05-12 01:06:45.652276+00:00',
    description: 'Bacon ipsum dolor sit amet swine strip steak frankfurter chicken,
      rump turkey venison kielbasa bacon pork chop filet mignon shank ham salami pork
      belly.', district: "Mutu\xE1", expiration: 2012-06-11, featured: 1, field: 5,
    flexible_hours: -1, food: -1, health: -1, min_semester: 0, modified: !!timestamp '2012-05-12
      03:41:03.061081+00:00', number: '72', relevance: -1, role: Vaga E, salary: '900',
    slug: '', state: 14, street: Rua Fernandes Mendonca, transport: -1, weekly_hours: 20}
  model: internships.internship
  pk: 7



    NEGOTIABLE_CHOICES = Choices(
    (-1, 'not_informed',    u'Não informar'), 
    ( 0, 'no',              u'Não'), 
    ( 1, 'negotiable',      u'A negociar'),
    ( 2, 'yes',             u'Sim'),
)

class Internship(TimeStampedModel, BRAddressModel):
    COMPANY_SIZES = Choices(
        ('peq',     'Pequeno Porte'), 
        ('med',     u'Médio Porte'),
        ('grd',     'Grande Porte'),
    )

    role            = models.CharField('Cargo', max_length=64)
    field           = models.ForeignKey('internships.Field')
    description     = models.TextField('Descrição')
    slug            = models.SlugField(blank=True)
    tags            = TaggableManager()



    weekly_hours    = models.PositiveSmallIntegerField('Carga horária', choices=[(20,'20'), (25, '25'), (30, '30')])
    salary          = models.DecimalField('Salário', max_digits=7, decimal_places=2, null=True)
    min_semester    = models.PositiveSmallIntegerField(default=0)



    # relevance index
    relevance       = models.IntegerField(default=-1)
    # Paid for top positions
    featured        = models.IntegerField(blank=True) 
    # Date internship will be removed from public site
    expiration      = models.DateField('Data de expiração')

    approved = models.BooleanField()
    active = models.BooleanField(default=True)

    objects = PassThroughManager.for_queryset_class(InternShipQuerySet)()

    def __unicode__(self):
        return self.role + ' na ' + self.company_name