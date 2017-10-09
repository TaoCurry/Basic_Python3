#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import logging
def use_logging(level):
    def decerator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warning('%s is running' % func.__name__)
            elif level == 'info':
                logging.warning('%s is running' % func.__name__)
            return func(*args)
        return wrapper
    return decerator
@use_logging(level='warn')
def foo(name='foo'):
    print('I am %s' % name)
foo()