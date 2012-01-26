#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.gis import admin

#from reversion import helpers

Term = models.get_model('nicetoknow', 'term')
Synonym = models.get_model('nicetoknow', 'synonym')

class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Term, TermAdmin)
admin.site.register(Synonym)

#helpers.patch_admin(Term)
#helpers.patch_admin(Synonym)
