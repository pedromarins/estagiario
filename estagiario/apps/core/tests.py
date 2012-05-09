# -*- coding: utf-8 -*-


from django.test import TestCase
from django.test.client import Client


class IndexPageTest(TestCase):
    
    def setUp(self):
        self.c = Client()


    def test_index_template(self):
        res = self.c.get('/')
        self.assertTemplateUsed(res, 'index.html')
