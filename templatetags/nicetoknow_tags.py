#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.db import models

Term = models.get_model('nicetoknow', 'term')

register = template.Library()

class RandomTermNode(template.Node):
    def __init__(self, random_term):
        self.random_term = random_term
        
    def render(self, context):
        context['term'] = self.random_term
        return ''

def get_random_term(parser, token):
    """
    Returns one random term as var 'term'
    
    i.e. {% get_random_term  %}
    """
    try:
        random_term = Term.objects.order_by('?')[0]
        return RandomTermNode(random_term)
    except IndexError:
        random_term = Term(title='Error', slug='error', description = 'No Term defined, please delete this Message or rename', source='http://trac.karrie.info/browser/repo/g2007/django_apps/nicetoknow/templatetags/nicetoknow_tags.py#L16')
        return RandomTermNode(random_term)
    
register.tag(get_random_term)