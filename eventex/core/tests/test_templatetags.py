# coding: utf-8
from django.test import TestCase
from django.template import Template, Context

class YoutubeTagTest(TestCase):
    def setUp(self):
        context     = Context({'ID': 1})
        template    = Template('{% load youtube %}{% youtube ID %}')
        self.content= template.render(context)
        
    def test_output(self):
        self.assertIn('<object', self.content)
        self.assertIn('/1', self.content)
        
#class SlideShareTagTest(TestCase):
    #TO-DO
    #def setUp(self):
        #context     = Context({'ID': 1},{'DOC': 'webinar-thefutureoffestivals1-140227041851-phpapp02'})
        #template    = Template('{% load slideshare %}{% slideshare ID %}{% slideshare DOC %}')
        #self.content= template.render(context)
        
    #def test_output(self):
        #self.assertIn('<object', self.content)
        #self.assertIn('/1/doc/webinar-thefutureoffestivals1-140227041851-phpapp02', self.content)
