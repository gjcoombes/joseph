#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Module: launch_job.py
Created on Thu Sep 05 12:22:17 2013
@author: gcoombes
Description:

"""
### Imports
from __future__ import print_function

import bonaparte.start as start
from bonaparte.datastructures import WinfatesTuple


### Logging ###
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
debug, info, error = logger.debug, logger.info, logger.error

### Constants
# WinfatesTuple = namedtuple("WinfatesTuple", "type_ exe core sink project stem q_group q_stage q_app")
### Classes

### Functions
def launch_job(stem):
    type_ = "winfates"
    exe = r"c:\simap\winfates.exe"
    core = "wahanda"
    sink = core
    project = "J0232_Murphy_Oil_Dunsborough-1"
    q_prefix = "test"
    q_stage = "start"
    q_app = type_

    tup = (type_, exe, core, sink, project, stem, q_prefix, q_stage, q_app)
    wftup = WinfatesTuple._make(tup)
    print(wftup)
    start.launch_job(wftup)

### Tests

def test_launch_job():
    stem = "SC7_TURTLE_DIESEL_136M3_b"
    launch_job(stem)




if __name__ == "__main__":
#    pytest.main(['test_datastructures.py', '--cov-report', 'html', '--cov', '.', '-xvv'])
    test_launch_job()
    print("Done __main__")
