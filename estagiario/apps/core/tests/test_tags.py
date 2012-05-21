# -*- coding: utf-8 -*-
import unittest
from django.conf import settings
from django.http import HttpRequest
from core.templatetags.menu_tags import active_field

class MenuTagsTest(unittest.TestCase):
    "tags from core.menu_tags"

    def _request(self, path):
        "mock GET request with <path>"
        req = HttpRequest()
        req.method = 'GET'
        req.path = path
        return req


    def test_active_field_default_css(self):
        "active_field using default css class"
        
        req = self._request('/engenharia/rj/')
        self.assertEqual(active_field(req, 'engenharia'), 'active')
        
        req = self._request('/contato/')
        self.assertEqual(active_field(req, 'engenharia'), '')


    def test_active_field_setting_css(self):
        "active_field using settings.CSS.field_menu_active"
        
        old = settings.CSS['field_menu_active']
        settings.CSS['field_menu_active'] = 'test_css'
        
        req = self._request('/direito/')
        self.assertEqual(active_field(req, 'direito'), 'test_css')


        req = self._request('/direito/')
        self.assertEqual(active_field(req, 'engenharia'), '')