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

### Constants

### Classes

### Functions
def index(request):
    return HttpResponse("Welcome to the winfates index.")

### Tests

if __name__ == "__main__":


    print("Done __main__")

