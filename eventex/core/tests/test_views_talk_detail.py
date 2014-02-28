# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk

class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(
            name = 'Henrique Bastos',
            slug = 'henrique-bastos',)
        self.resp = self.client.get(r('core:talk_detail',args=[1]))

    def test_get(self):
        'GET should return status code 200.'		
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should de core/talk_detail.html'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')
    
    def test_context(self):
        'Talk must be in context'
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)
        
    def test_not_found(self):
        url = r('core:talk_detail', args=[0])
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
    
    def test_html(self):
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/henrique-bastos')
        self.assertContains(self.resp, 'Henrique Bastos')
        
