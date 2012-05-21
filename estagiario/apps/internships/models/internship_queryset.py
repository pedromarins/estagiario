# -*- coding: utf-8 -*-

from datetime import date
from django.db import models
from field import Field
from django.db.models.query import QuerySet

class InternShipQuerySet(QuerySet):
    
    by_city     = lambda x,y: x.filter(x, city=y)
    by_state    = lambda x,y: x.filter(x, state=y)
    by_uf       = lambda x,y: x.filter(x, state__uf=y)

    company_size    = lambda x,y: x.filter(x, company_size=y)
    weekly_hours    = lambda x,y: x.filter(x, weekly_hours=y)


    def is_active(self, v=True):
        return self.filter(active=v)

    def is_approved(self, v=True):
        return self.filter(approved=v)

    def is_expired(self):
        
        return self.filter(expiration__lt=date.today())
        
    def not_expired(self):
        print date.today()
        return self.filter(expiration__gte=date.today())
    

    def available(self):
        "internships that are not expired and should be displayed on website"
        return self.is_active().is_approved().not_expired()


    def by_text(self, text):
        raise Exception('implement text search')

    def by_tag(self, tag):
        return self.filter(tags=tag)




    # role            = models.CharField('Cargo', max_length=64)
    # field           = models.ForeignKey('internships.Field')
    # description     = models.TextField('Descrição')
    # slug            = models.SlugField(blank=True)
    # tags            = TaggableManager()

    # company_name    = models.CharField('Empresa', max_length=64)

    # min_semester    = models.PositiveSmallIntegerField(default=0)

    # transport
    # health
    # food
    # flexible_hours
