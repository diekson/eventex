# coding: utf-8
from django.test.utils import override_settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend
#from unittest import skip

#@skip
class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
                username='diekson',
                email   ='diekson@live.com',
                password= 'senha',)                
        self.backend = EmailBackend()
        
    def test_autenticate_with_email(self):
        user = self.backend.authenticate(
                email   ='diekson@live.com',
                password='senha',)        
        self.assertIsNotNone(user)
        
    def test_wrong_password(self):
        user = self.backend.authenticate(
                email   ='diekson@live.com',
                password= 'elado',)        
        self.assertIsNone(user)
        
    def test_unknown_user(self):
        user = self.backend.authenticate(
                email   ='email@elado.com',
                password='senha',)
        self.assertIsNone(user)
        
    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))
 
#@skip       
class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
                username='user1',
                email   ='diekson@live.com',
                password= 'senha',)
        UserModel.objects.create_user(
                username='user2',
                email   ='diekson@live.com',
                password= 'senha',)           
        self.backend = EmailBackend()
    
    def test_multiple_emails(self):
        user = self.backend.authenticate(
                email   ='diekson@live.com',
                password='senha',)  
        self.assertIsNone(user)

#@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(
                username='diekson',
                email   ='diekson@live.com',
                password= 'senha',)
    
    def test_login_with_email(self):
        result = self.client.login(
                email   ='diekson@live.com',
                password='senha',)  
        self.assertTrue(result)
        
    
    def test_login_with_username(self):
        result = self.client.login(
                username='diekson@live.com',
                password='senha',)  
        self.assertTrue(result)
    
