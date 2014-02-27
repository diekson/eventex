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
        
    def test_email_or_phone(self):
        'Informar email ou telefone'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
    
    def test_name_must_be_capitalized(self):
        'Name capitalized'
        form = self.make_validated_form(name='DIEKSON scardine')
        self.assertEqual('Diekson Scardine', form.cleaned_data['name'])
        
    def make_validated_form(self, **kwargs):
        data = dict(
            name='Diekson Scardine',
            email='diekson@live.com',
            cpf='12345678901',
            phone_0='21',
            phone_1='35538214',
        )
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
        
