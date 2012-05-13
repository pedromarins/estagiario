# -*- coding: utf-8 -*-

from datetime import datetime, date
from django.db import models
from django.db.models.query import QuerySet

class InternShipQuerySet(QuerySet):
    
    def is_active(self, v=True):
        return self.filter(active=v)

    def is_approved(self, v=True):
        return self.filter(approved=v)

    not_expired = lambda x: x.filter(expiration__gt=date.today())
    is_expired = lambda x: x.filter(expiration__lte=date.today())

    def available(self):
        return self.is_active().is_approved().not_expired()

    def by_city(self, city):
        return self.filter(city=city)

    def by_state(self, state):
        return self.filter(state=state)

    def by_state_uf(self, uf):
        return self.filter(state__uf=uf)


    def company_size(self, size):
        return self.filter(company_size=size)

    def weekly_hours(self, hours):
        return self.filter(weekly_hours=hours)

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
