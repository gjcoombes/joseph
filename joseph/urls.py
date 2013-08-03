#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: urls.py
Created on Sun Aug 04 00:02:22 2013
@author: gav
Description:

"""
### Imports
from __future__ import print_function
from __future__ import absolute_import

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joseph.views.home', name='home'),
    # url(r'^joseph/', include('joseph.foo.urls')),
    url(r'^winfates/', include('winfates.urls', namespace="winfates")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

### Constants

### Classes

### Functions

### Tests

if __name__ == "__main__":


    print("Done __main__")

