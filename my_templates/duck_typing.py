#duck_typing.py

import inspect

class Abstract1(object):
    def get(self):
        raise NotImplementedError("Class %s doesn't implement method %s()" % (self.__class__.__name__, inspect.stack()[0][3]))
    def set(self, value):
        raise NotImplementedError("Class %s doesn't implement method %s()" % (self.__class__.__name__, inspect.stack()[0][3]))
    
class BaseFull(Abstract1):
    _value = 'Default value'
    def get(self):
        return self._value
    def set(self, value):
        self._value = value
        
class BasePartial(Abstract1):
    _value = 'Partial base'
    def get(self):
        return self._value
    
c1 = BaseFull()
print c1.get()
c1.set('A new value.')
print c1.get()

try:
    c2 = BasePartial()
    print c2.get()
    c2.set('This should never work.')
    print c2.get()
except Exception, err:
    print 'Error:'+str(err)