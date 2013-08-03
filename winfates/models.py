#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: models.py
Created on Sat Aug 03 17:09:47 2013
@author: gav
Description: Django models for the winfates app

"""
### Imports
from __future__ import print_function
from __future__ import absolute_import

from django.db import models
import datetime
from django.utils import timezone

### Constants

### Classes
class Machine(models.Model):
    """Represents one physical computer box
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    team = models.CharField(max_length=128,
                            help_text="apache or woodside?")
    cores = models.IntegerField()
    ram = models.IntegerField(verbose_name="RAM")
    bitset = models.CharField(max_length=16)
    ip_address = models.IPAddressField(blank=True,
                                       verbose_name="IP Address")

    def __unicode__(self):
        return self.name

    def is_apache(self):
        return self.team.lower() == "apache"

class Project(models.Model):
    """

    eg J0236 Apache Ennerdale-1
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    client = models.CharField(max_length=128)
    job_number = models.CharField(max_length=8)
    project_dir = models.CharField(max_length=128)

class Scenario(models.Model):
    """
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    oil = models.CharField(max_length=128)
    base_in3 = models.TextField()

class Season(models.Model):
    """
    """
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    months = models.CharField(max_length=128)
    days = models.IntegerField()

class Run(models.Model):
    """
    """
    name = models.CharField(max_length=128)
    stem = models.CharField(max_length=128)

### Functions

### Tests

if __name__ == "__main__":


    print("Done __main__")

