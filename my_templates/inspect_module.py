#inspect_module.py
'''
A rather useful little thing which lets you look through the stack during 
execution. Handy for introspection.
'''
import inspect

def foo():
    print 'Inside function {}'.format(inspect.stack()[0][3],)
    print 'Which was called by {}'.format(inspect.stack()[1][3],)
    
if __name__ == '__main__':
    foo()