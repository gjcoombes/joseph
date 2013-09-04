#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: find.py
Created on Wed Sep 04 22:09:01 2013
@author: gav
Description: Find records of jobs in mongodb

"""
### Imports
from __future__ import print_function

from pymongo import MongoClient
### Logging ###
import logging
logging.basicConfig(level=logging.DEBUG)
debug, info, error = logging.debug, logging.info, logging.error

### Constants
MONGO_ADDR = 'mongodb://tornado:27017/'
MONGO_DB = 'bonaparte_log'
MONGO_COLLECTION = 'message_atoms'
### Classes

### Functions ###
def filter_(ma):
    return {
        "host": ma["host"],
        "stage": ma['q_stage'],
        "time_recv": ma["time_recv"],
        "time_sent": ma["time_sent"],
    }

def my_print(ma):
    tpl = "host: {h}, sent: {ts}, recv: {tr}, stage: {s}"
    rec = tpl.format(h=ma["host"],
                     tr=ma["time_recv"].strftime("%H:%M:%S"),
                     ts=ma["time_sent"].strftime("%H:%M:%S"),
                     s=ma["stage"])
    print(rec)

### Tests

if __name__ == "__main__":

    # setup
    client = MongoClient(MONGO_ADDR)
    db = client.bonaparte_log
    atoms = db.bonaparte_log

    #validate stem
#    stem = "DIESEL_XENA_Q1_019"
    stem = "DIESEL_XENA_Q3_074"
    query = {
        "stem": stem
    }
    # return elements with stem
    for job in atoms.find(query).sort("time_recv"):
        print(job)
        print()
#        display_atom = filter_(job)
#        my_print(display_atom)


    print("Done __main__")

