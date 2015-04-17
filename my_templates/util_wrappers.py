#!/usr/bin/env python

'''
This contains utility decotrators for doing a variety of things.
'''

import threading


def echo(func):
    '''
    This prints a function's name, location and arguments for ease of
    debugging.
    '''
    def _format_args(arg_val):
        arg, val = arg_val
        return '%s=%r' % (arg, val)

    def wrapper(*args, **kwargs):
        try:
            print 'Function name: %s' % (func.__name__, )
            code = func.__code__
            argcount = code.co_argcount
            argnames = code.co_varnames[:argcount]
            defaults = func.__defaults__ or list()
            argdefs = dict(list(zip(argnames[-len(defaults):], defaults)))
            print 'Function arguments:'
            print '    Positional: ', list(map(_format_args,
                                               list(zip(argnames, args))))
            print '    Defaulted : ', [_format_args((a, argdefs[a]))
                                       for a in argnames[len(args):]
                                       if a not in kwargs]
            print '    Nameless  : ', list(map(repr, args[argcount:]))
            print '    Keyword   : ', list(map(_format_args,
                                               list(kwargs.items())))
            return func(*args, **kwargs)
        except Exception, err:
            print 'Echo wrapper could not describe the function.\n', str(err)
            return func(*args, **kwargs)
    return wrapper

def synchronized(lock=None):
    '''
    Synchronizes a function by assigning it a mutex lock.
    TODO: Test this. Use at your own risk. I haven't tested this yet - Puneet
    '''
    if lock is None:
        lock = threading.Lock()
        
    def wrapper(func):
        def new_func(*args, **kwargs):
            lock.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                lock.release()
        return new_func
    return wrapper
            


#=========================================================================
# class TstClass(object):
#     @echo
#     def test_f(self, a, b='bar'):
#         print 'Test function in class'
#
# if __name__ == '__main__':
#     @echo
#     def test_func(a, b, c='foo', d=0):
#         print 'This is a test function.'
#
#     test_func('blah', 42)
#
#     class_instance = TstClass()
#     class_instance.test_f(0)
#=========================================================================
