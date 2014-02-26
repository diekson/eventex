# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Diekson Scardine',
            cpf='12345678901',
            email='diekson@live.com',
            phone='21-35538214',
        )
        
    def test_create(self):
        'Subscription must have name, cpf, email, phone.'
        self.obj.save()
        self.assertEqual(1,self.obj.pk)
        
    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at,datetime)
        
    def test_unicode(self):
        'Name must be unicode'
        self.assertEqual(u'Diekson Scardine',unicode(self.obj))
        
    def test_paid_default_value_is_False(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)



class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(name='Diekson Scardine', cpf='12345678901',email='diekson@live.com',phone='21-35538214')
        
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Diekson Scardine', cpf='12345678901',email='eu@live.com',phone='21-35538214')
        self.assertRaises(IntegrityError, s.save)
        
    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Diekson Scardine', cpf='02345678901',email='diekson@live.com',phone='21-35538214')
        self.assertRaises(IntegrityError, s.save)
