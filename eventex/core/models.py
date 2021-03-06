# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager

class Speaker(models.Model):
    name        = models.CharField(_('Nome'), max_length=255)
    slug        = models.SlugField(_('Slug'))
    url         = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)
    
    class Meta:
        verbose_name        = _('palestrante')
        verbose_name_plural = _('palestrantes')
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
            return ('core:speaker_detail', (), {'slug': self.slug})

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('Email')),
        ('F', _('Fax')),
    )
    
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind    = models.CharField(_('tipo'),max_length=1, choices=KINDS)
    value   = models.CharField(_('valor'), max_length=255)
    
    objects = models.Manager()
    emails  = KindContactManager('E')
    phones  = KindContactManager('P')
    faxes   = KindContactManager('F')    
    
    def __unicode__(self):
        return self.value



    
class Talk(models.Model):
    title       = models.CharField(_('Título'),max_length=200)
    description = models.TextField(_('Descrição'))
    start_time  = models.TimeField(_('Horário'), blank=True)
    speakers    = models.ManyToManyField('Speaker', verbose_name=_('palestrantes'))
    
    objects     = PeriodManager()
    
    class Meta:
        verbose_name        = _('palestra')
        verbose_name_plural = _('palestras')
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('core:talk_detail', (), {'pk': self.pk})
    
    @property
    def videos(self):
        return self.media_set.filter(kind='YT')
    
    #@property
    #def slides(self):
        #return self.media_set.filter(kind='SL')

class Course(Talk):
    slots = models.IntegerField(_('vagas'))
    notes = models.TextField(_(u'observações'))
    
    objects     = PeriodManager()
    
class Media(models.Model):
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SL', _('SlideShare')),
    )
    
    talk        = models.ForeignKey('Talk', verbose_name=_('palestra'))
    kind        = models.CharField(_('tipo'), max_length=2, choices=MEDIAS)
    title       = models.CharField(_(u'título'), max_length=255)
    media_id    = models.CharField(_('ref'), max_length=255)
        
    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)
