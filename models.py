#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify

class Term(models.Model):
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    source      = models.URLField()

    class Meta:
        ordering = ['title']
        verbose_name = u'Definition'
        verbose_name_plural = u'Definitionen'

    def __unicode__(self):
        return unicode(self.title)
    
    def save(self):
        if not len(self.slug):
            self.slug = slugify(self.title)
        super(Term, self).save()
    

class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term  = models.ForeignKey(Term, related_name="synonyms")
    
    class Meta:
        ordering = ['title']
        verbose_name = u'Synonym'
        verbose_name_plural = u'Synonyme'

    def __unicode__(self):
        return u"%s (synonym for %s)" % (self.title, self.term.title)
