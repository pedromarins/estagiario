# -*- coding: utf-8 -*-

class dotdic(dict):
    def __getattr__(self, k):
        try:
            return self.__getitem__(k)
        except Exception:
            return ''