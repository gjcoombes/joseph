#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: admin.py
Created on Sat Aug 03 16:45:56 2013
@author: gav
Description: Expose winfates app to django-admin

"""
### Imports
from __future__ import print_function
from __future__ import absolute_import


from django.contrib import admin
from winfates.models import Machine, Project, Scenario, Season, Run

admin.site.register((Machine, Project, Scenario, Season, Run))

### Constants

### Classes

### Functions

### Tests

if __name__ == "__main__":


    print("Done __main__")

