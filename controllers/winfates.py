#! /usr/bin/env python 2
#! encoding: utf-8
"""

"""
import bonaparte
import winfates


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return {
        "message": "Joseph says hello again monkeys!",
        "counter": session.counter
    }


def first():
    form = SQLFORM.factory(Field('visitor_name',
                                 label='what is your name?',
                                 requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)

def second():
    if not request.function=='first' and not session.visitor_name:
        redirect(URL('first'))
    return dict()

def find():
    form = SQLFORM.factory(
        Field('stem',
            label='which stem? e.g. j0256_dies_q1_001',
            requires=IS_NOT_EMPTY()),
        )
    if form.process().accepted:
        session.stem= form.vars.stem
        redirect(URL('found'))
    return dict(form=form)

def found():
    if not request.function=='find' and not session.stem:
        redirect(URL('find'))
    return dict()

def find():
    form = SQLFORM.factory(
        Field('stem',
            label='which stem?',
            requires=IS_NOT_EMPTY()),
        )
    if form.process().accepted:
        session.stem= form.vars.stem
        redirect(URL('found'))
    return dict(form=form)

def launch_my_job():
    form = SQLFORM.factory(
        Field('q_app',
            label='which app?',
            requires=IS_NOT_EMPTY()),
        Field('core',
            label='which core machine?',
            requires=IS_NOT_EMPTY()),
        Field('sink',
            label='which sink machine?',
            requires=IS_NOT_EMPTY()),
        Field('project',
            label='which project folder?',
            requires=IS_NOT_EMPTY()),
        Field('stem',
            label='which stem?',
            requires=IS_NOT_EMPTY()),
        Field('q_group',
            label='which queue group?',
            requires=IS_NOT_EMPTY()),

        )
    if form.process().accepted:
#        stem = form.vars.stem
#        winfates.launch.launch_job(stem)
        redirect(URL('launched'))
    return dict(form=form)

def launched():
    if not request.function=='launch_my_job' and not session.stem:
        redirect(URL('launch_my_job'))
    return dict()





if __name__ == "__main__":

    print("Done __main__")







