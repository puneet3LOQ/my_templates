#/home/puneet/puneet/workspace/my_templates/how_to_wrapper.py
'''
How to write a wrapper function.
'''

def test_wrapper(func):
    def do_stuff_and_proceed(*args, **kwargs):
        print 'test_wrapper called!'
        return func(*args, **kwargs)
    return do_stuff_and_proceed

def foo():
    print 'Foo called.'
    
@test_wrapper
def bar():
    print 'Bar called.'

if __name__ == '__main__':
    foo()
    bar()