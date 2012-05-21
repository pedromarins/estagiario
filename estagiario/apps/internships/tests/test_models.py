# -*- coding: utf-8 -*-
from django.utils import unittest

from datetime import date, timedelta
import factory
from factories import StateFactory, FieldFactory, InternshipFactory, fill_address
from internships.models import Internship



factory.Factory.default_strategy = factory.CREATE_STRATEGY
#InternshipFactory.default_strategy = factory.BUILD_STRATEGY
def next_days(dt, days):
    return dt + timedelta(days=days)


    
class InternshipQuerysetTest(unittest.TestCase):
    def setUp(self):
        StateFactory.make_for_test()
        FieldFactory.make_for_test()
        
        self.today = date.today()
        self.tomorow = today + timedelta(days=1)
        self.yesterday = today - timedelta(days=1)


    def test_available_expired(self):
        '''
            Internship.objects.available() should respect expiration dates 
        '''
        
        ins = InternshipFactory(expiration=self.yesterday)        
        self.assertNotIn(ins, Internship.objects.available() )

        ins = InternshipFactory(expiration=self.today)        
        self.assertIn(ins, Internship.objects.available() )

        ins = InternshipFactory(expiration=self.tomorow)        
        self.assertIn(ins, Internship.objects.available() )


        print ins.expiration
        ins = InternshipFactory(expiration=date(2012,3,6))
        self.assertIn(ins, Internship.objects.available())
        #print ins.expiration
        #print Internship.objects.all()
        print Internship.objects.filter(expiration__gte=date(2012,3,6))
        


#     def test
#         """
#         #print datetime.date.today()
#         # self.assertEqual(self.cat.speak(), 'The cat says "meow"')
    
#         # expiration      = models.DateField('Data de expiração')

    
#         # approved = models.BooleanField() # if False, should never be displayed
#         # active = models.BooleanField(default=True)

#             expired should not be shown on available
#             inactive or unapproved too

#             f is_expired(self, status=True):
#         op = 'lt' if status else 'gte'
#         return self._filter_op('expiration', op, date.today())

#     not_expired = lambda x: x.is_expired(status=False)
    

#     def available(self):
#         "internships that are not expired and should be displayed on website"
#         return self.is_active().is_approved().not_expired()

#         """


# class SizeFilterTest(unittest.TestCase):
#     pass



