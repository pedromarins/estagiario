# -*- coding: utf-8 -*-
from django.db.models.query import QuerySet

class BaseQuerySet(QuerySet):

    def _filter_op(self, field, op, val):
        return self.filter(**{field +'__'+op: val})

    def _exclude_op(self, field, op, val):
        return self.exclude(**{field +'__'+op: val})
    