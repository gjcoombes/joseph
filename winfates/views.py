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
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from winfates.models import Sighting, Machine
### Constants

### Classes

### Functions
def index(request):
    latest_sighting_list = Sighting.objects.order_by('-time_recv')[:3]
    context = {"latest_sighting_list": latest_sighting_list}
    return render(request, 'winfates/index.html', context)

def machine(request, machine_id):
    mach = get_object_or_404(Machine, pk=machine_id)
    return render(request, 'winfates/machine.html', {'machine': mach})

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

