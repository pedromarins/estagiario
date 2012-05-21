# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from splinter.browser import Browser
import unittest

class LocalTest(object):
    
    def _url(self, path, host='localhost', port=8000):
        return 'http://%s:%d/%s' % (host, port, path)


class IndexTest(unittest.TestCase, LocalTest):
    
    @classmethod
    def setUpClass(cls):
        #cls.browser = Browser()        
        #cls.browser = Browser('zope.testbrowser')
        cls.browser = Browser('chrome')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


    def tearDown(self):
        pass # Post.objects.all().delete()

    def visit(self, url):
        self.browser.visit(self._url(url))

    def test_state_filter_empty(self):
        "test empty select if there's no filter or url for state "
        self.visit('estagios/')        
        select =  self.browser.find_by_name('stateselect').first
        self.assertEqual(select.value, 'estagios')

        self.visit('direito/')        
        select =  self.browser.find_by_id('id-state-select').first
        self.assertEqual(select.value, 'estagios')
    

    def test_state_filter_val(self):
        "state filter"
        self.visit('estagios/sp/')        
        # select =  self.browser.find_by_id('id-state-select').first
        # self.assertEqual(select.value, 'sp')


        # self.visit('direito/sp/')        
        # select =  self.browser.find_by_id('id-state-select').first
        # self.assertEqual(select.value, 'sp')
        
        
        self.browser.select('stateselect', 'rj')      
        self.browser.url
        select = self.browser.find_by_id('id-state-select').first
        #self.assertEqual(select.value, 'rj')
        self.browser.url
        print self.browser.find_option_by_text('São Gonçalo')


        #print self.browser.find_by_tag('option')[0].text
        #print self.browser.find_by_tag('option')[0].value

        
        # print dir(self.browser.find_by_css('.fb-login').first)
        # print self.browser.find_by_css('.fb-login').first.text
        #self.assertEqual(1 + 1, 2)

class DetailInternshipTest(unittest.TestCase, LocalTest):
    
    @classmethod
    def setUpClass(cls):
        #cls.browser = Browser()        
        cls.browser = Browser('zope.testbrowser')
    
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


    def tearDown(self):
        pass # Post.objects.all().delete()


    def test_basic_addition(self):
        #print self.live_server_url
        # url = self._url('/estagios/')
        # self.browser.visit(url)
        
        # print dir(self.browser.find_by_css('.fb-login').first)
        # print self.browser.find_by_css('.fb-login').first.text
        #self.assertEqual(1 + 1, 2)
        

        pass

        #assert browser.is_text_present('foo')
        #taps pull mysql://root:root@localhost/provaessa mysql://e62567b250a018:84566341@us-mm-auto-dca-01.cleardb.com/heroku_fcac7a5e84060e9


        

# from django_liveserver.testcases import LiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver


# class MySeleniumTests(LiveServerTestCase):
#     #fixtures = ['test-data.json']

#     @classmethod
#     def setUpClass(cls):
#         cls.selenium = WebDriver()
#         super(MySeleniumTests, cls).setUpClass()

#     @classmethod
#     def tearDownClass(cls):
#         super(MySeleniumTests, cls).tearDownClass()
#         cls.selenium.quit()

#     def test_hello(self):
#         self.selenium.get(self.live_server_url)
#         self.assertIn("Hello World", self.selenium.title)


