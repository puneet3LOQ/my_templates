import abc
import inspect

#Declaring abstract methods by meta classing ABCMeta
class TestBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def set(self, value):
        '''
        Setter function.
        '''
        #This is actually of no use.
        #abc.abstractmethod causes an exception to be raised automatically if a derived class doesn't implement this method.
        #This exception is raised only on instantiation though. Not at compile time.
        raise NotImplementedError("Class %s doesn't implement method %s()" % (self.__class__.__name__, inspect.stack()[0][3]))
    @abc.abstractmethod
    def get(self):
        '''
        Getter function.
        '''
        pass
    
#Registering a concrete class by calling the ABCMeta.register function.
class TestConcreteRegister(object):
    def set(self, value):
        self.value = value
    def get(self):
        return self.value
TestBase.register(TestConcreteRegister)

#Testing to see if TestConcreteRegister is seen as a subclass or an instance.
print 'TestConcreteRegister subclass', issubclass(TestConcreteRegister, TestBase) #True
print 'TestConcreteRegister instance', isinstance(TestConcreteRegister(), TestBase) #True

#Registering a concrete class by inheriting the abstract class
class TestConcreteInherit(TestBase):
    def set(self, value):
        self.value = value
    def get(self):
        return self.value

#Testing to see if TestConcreteInherit is seen as a subclass or an instance.
print 'TestConcreteInherit subclass:', issubclass(TestConcreteInherit, TestBase) #True
print 'TestConcreteInherit instance:', isinstance(TestConcreteInherit(), TestBase) #True
    
#Incompletely implemented classes can be registered
class IncompleteRegister(object):
    def set(self, value):
        self.value = value
TestBase.register(IncompleteRegister)

#Testing to see if TestConcreteInherit is seen as a subclass or an instance.
print 'IncompleteRegister subclass:', issubclass(IncompleteRegister, TestBase)#True
print 'IncompleteRegister instance:', isinstance(IncompleteRegister(), TestBase) #True

#Incompletely implemented classes cannot inherit from an abstract.
class IncompleteInherit(TestBase):
    def set(self, value):
        self.value = value

#Testing to see if TestConcreteInherit is seen as a subclass or an instance.
print 'IncompleteInherit subclass:', issubclass(IncompleteInherit, TestBase) #True
try:
    print 'IncompleteInherit instance:', isinstance(IncompleteInherit(), TestBase) #False This errors out on trying to instantiate.
except Exception, err:
    print 'Error:' + str(err)

#Checking to see what classes TestBase sees as it's subclasses
#Note to self: Prefer inheritance over registration for better introspection.
print 'Subclasses as seen by TestBase.__subclasses__()'
for sc in TestBase.__subclasses__():
    print sc.__name__

print '\nInstantiating each class:'
c1 = TestConcreteRegister();
c2 = TestConcreteInherit();
c3 = IncompleteRegister();
try:
    c4 = IncompleteInherit(); #This errors out on trying to instantiate.
except Exception, err:
    print 'Error:' + str(err)

#ABCs can have concrete methods which MUST be instantiated by derived classes to be used.
class ConcreteABC(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get(self):
        return 'ConcreteABC getter called.'
    
class InheritConcreteABC(ConcreteABC):
    def get(self):
        print super(InheritConcreteABC, self).get()
        print 'InheritConcreteABC getter called.'
        
c5 = InheritConcreteABC()
c5.get()
    
#Properties can be declared abstract as well. (With or without decorator syntax)
class PropertyBase(object):
    __metaclass__ = abc.ABCMeta
    
    @property
    def value(self):
        return 'Control should never reach here.'
    @value.setter
    def value(self, newvalue):
        return
    
class PropertyConcrete(PropertyBase):
    _value = 'Some old value'
    
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newvalue):
        self._value = newvalue
        
print 
c6 = PropertyConcrete()
print 'Old value: ', c6.value
c6.value = 'Some new value.'
print 'New value: ', c6.value
    
