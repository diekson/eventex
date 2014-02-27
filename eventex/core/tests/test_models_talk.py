# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
                title       = u'Introdução ao Django',
                description = u'Descrição da Palestra',
                start_time  = '10:00')
                
    def test_create(self):
        'Talk instance should be saved'
        self.assertEqual(1, self.talk.pk)
        
    def test_unicode(self):
        'Talk string introduction should be de name.'
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))
    
    def test_speakers(self):
        'Talk has many Speakers and vice-versa'
        self.talk.speakers.create(
                name='Henrique Bastos',
                slug='henrique-bastos',
                url='http://henriquebastos.net')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be instance of PreiodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)

class CourseModelTest(TestCase)
    def setUp(self):
        self.couse = Course.objects.create(
                title       = u'Tutorial Django',
                description = u'Descrição do Palestra',
                start_time  = '10:00')
                
    def test_create(self):
        'Talk instance should be saved'
        self.assertEqual(1, self.talk.pk)
        
    def test_unicode(self):
        'Talk string introduction should be de name.'
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))
    
    def test_speakers(self):
        'Talk has many Speakers and vice-versa'
        self.talk.speakers.create(
                name='Henrique Bastos',
                slug='henrique-bastos',
                url='http://henriquebastos.net')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be instance of PreiodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)
