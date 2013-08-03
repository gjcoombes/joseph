#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: urls.py
Created on Sat Aug 03 22:40:50 2013
@author: gav
Description: urls for winfates app

"""
### Imports
from __future__ import print_function
from __future__ import absolute_import
from django.conf.urls import patterns, url

from winfates import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^machine/(?P<machine_id>\d+)/$',  views.machine,  name='machine'),
    url(r'^sighting/(?P<sighting_id>\d+)/$', views.sighting, name='sighting'),
    url(r'^location/(?P<sighting_id>\d+)/$', views.location, name='location'),
    url(r'^latest-sightings/$', views.latest_sightings, name='latest_sightings'),
)
### Constants

### Classes

### Functions

### Tests

if __name__ == "__main__":


    print("Done __main__")

