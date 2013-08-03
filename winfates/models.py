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


class Sighting(models.Model):
    """ An interval where the winfates message was possessed/transformed/seen
    """
    machine = models.ForeignKey(Machine)
    time_recv = models.DateTimeField()
    time_sent = models.DateTimeField()
    msg_id = models.CharField(max_length=128)
    queue = models.CharField(max_length=128)
    stem = models.CharField(max_length=128)
    exe = models.CharField(max_length=128)

### Functions

### Tests

if __name__ == "__main__":


    print("Done __main__")

