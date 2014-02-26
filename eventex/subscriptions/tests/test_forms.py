# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_hasfields(self):
        'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name','email','cpf','phone'],form.fields)
        
    def test_cpf_is_digit(self):
        'cpf must only accept digits'
        form = self.make_validated_form(cpf='1234567890a')      
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_cpf_11_digits(self):
        'cpf must have 11 digits'
        form = self.make_validated_form(cpf='123')        
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_email_is_optional(self):
        'Email optional'
        form = self.make_validated_form(email='')      
        self.assertFalse(form.errors)
        
    def make_validated_form(self, **kwargs):
        data = dict(
            name='Diekson Scardine',
            cpf='12345678901',
            email='diekson@live.com',
            phone='21-35538214',
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
        
