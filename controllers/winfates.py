#! /usr/bin/env python 2
#! encoding: utf-8
"""

"""

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
    if not request.function=='first' and not session.visitor_name:
        redirect(URL('found'))  
    return dict()