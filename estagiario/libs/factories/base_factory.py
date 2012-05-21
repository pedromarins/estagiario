# -*- coding: utf-8 -*-

class BaseFactory(object):
    
    @classmethod
    def _make(cls, save, **kwargs):
        if save:
            return cls.create(**kwargs)
        else:
            return cls.build(**kwargs)