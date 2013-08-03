#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: views.py
Created on Sat Aug 03 22:34:36 2013
@author: gav
Description: Views for the winfates app

"""
### Imports
from __future__ import print_function
from __future__ import absolute_import

from django.http import HttpResponse
from django.template import RequestContext, loader


from winfates.models import Sighting
### Constants

### Classes

### Functions
def index(request):
    latest_sighting_list = Sighting.objects.order_by('-time_recv')[:3]
    template = loader.get_template('winfates/index.html')
    context = RequestContext(request, {
        "latest_sighting_list": latest_sighting_list,
        })
    return HttpResponse(template.render(context))

def machine(request, machine_id):
    return HttpResponse("You are looking at machine {}".format(machine_id))

def sighting(request, sighting_id):
    return HttpResponse("You are looking at sighting {}".format(sighting_id))

def location(request, sighting_id):
    return HttpResponse("You are looking for sighting {}".format(sighting_id))

def latest_sightings(request):
    latest = Sighting.objects.order_by('-time_recv')[:1]
    text = "The last sighting was {}".format(latest.id)
    return HttpResponse(text)

### Tests

if __name__ == "__main__":


    print("Done __main__")

