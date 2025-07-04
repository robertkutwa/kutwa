# encoding: utf-8
# module _operator
# from (built-in)
# by generator 1.147
"""
Operator interface.

This module exports a set of functions implemented in C corresponding
to the intrinsic operators of Python.  For example, operator.add(x, y)
is equivalent to the expression x+y.  The function names are those
used for special methods; variants without leading and trailing
'__' are also provided for convenience.
"""
# no imports

# functions

def abs(a): # real signature unknown; restored from __doc__
    """ Same as abs(a). """
    pass

def add(*args, **kwargs): # real signature unknown
    """ Same as a + b. """
    pass

def and_(*args, **kwargs): # real signature unknown
    """ Same as a & b. """
    pass

def call(*args, **kwargs): # real signature unknown
    """ Same as obj(*args, **kwargs). """
    pass

def concat(*args, **kwargs): # real signature unknown
    """ Same as a + b, for a and b sequences. """
    pass

def contains(*args, **kwargs): # real signature unknown
    """ Same as b in a (note reversed operands). """
    pass

def countOf(*args, **kwargs): # real signature unknown
    """ Return the number of items in a which are, or which equal, b. """
    pass

def delitem(*args, **kwargs): # real signature unknown
    """ Same as del a[b]. """
    pass

def eq(*args, **kwargs): # real signature unknown
    """ Same as a == b. """
    pass

def floordiv(*args, **kwargs): # real signature unknown
    """ Same as a // b. """
    pass

def ge(*args, **kwargs): # real signature unknown
    """ Same as a >= b. """
    pass

def getitem(*args, **kwargs): # real signature unknown
    """ Same as a[b]. """
    pass

def gt(*args, **kwargs): # real signature unknown
    """ Same as a > b. """
    pass

def iadd(*args, **kwargs): # real signature unknown
    """ Same as a += b. """
    pass

def iand(*args, **kwargs): # real signature unknown
    """ Same as a &= b. """
    pass

def iconcat(*args, **kwargs): # real signature unknown
    """ Same as a += b, for a and b sequences. """
    pass

def ifloordiv(*args, **kwargs): # real signature unknown
    """ Same as a //= b. """
    pass

def ilshift(*args, **kwargs): # real signature unknown
    """ Same as a <<= b. """
    pass

def imatmul(*args, **kwargs): # real signature unknown
    """ Same as a @= b. """
    pass

def imod(*args, **kwargs): # real signature unknown
    """ Same as a %= b. """
    pass

def imul(*args, **kwargs): # real signature unknown
    """ Same as a *= b. """
    pass

def index(*args, **kwargs): # real signature unknown
    """ Same as a.__index__() """
    pass

def indexOf(*args, **kwargs): # real signature unknown
    """ Return the first index of b in a. """
    pass

def inv(*args, **kwargs): # real signature unknown
    """ Same as ~a. """
    pass

def invert(*args, **kwargs): # real signature unknown
    """ Same as ~a. """
    pass

def ior(*args, **kwargs): # real signature unknown
    """ Same as a |= b. """
    pass

def ipow(*args, **kwargs): # real signature unknown
    """ Same as a **= b. """
    pass

def irshift(*args, **kwargs): # real signature unknown
    """ Same as a >>= b. """
    pass

def isub(*args, **kwargs): # real signature unknown
    """ Same as a -= b. """
    pass

def is_(*args, **kwargs): # real signature unknown
    """ Same as a is b. """
    pass

def is_not(*args, **kwargs): # real signature unknown
    """ Same as a is not b. """
    pass

def itruediv(*args, **kwargs): # real signature unknown
    """ Same as a /= b. """
    pass

def ixor(*args, **kwargs): # real signature unknown
    """ Same as a ^= b. """
    pass

def le(*args, **kwargs): # real signature unknown
    """ Same as a <= b. """
    pass

def length_hint(*args, **kwargs): # real signature unknown
    """
    Return an estimate of the number of items in obj.
    
    This is useful for presizing containers when building from an iterable.
    
    If the object supports len(), the result will be exact.
    Otherwise, it may over- or under-estimate by an arbitrary amount.
    The result will be an integer >= 0.
    """
    pass

def lshift(*args, **kwargs): # real signature unknown
    """ Same as a << b. """
    pass

def lt(*args, **kwargs): # real signature unknown
    """ Same as a < b. """
    pass

def matmul(*args, **kwargs): # real signature unknown
    """ Same as a @ b. """
    pass

def mod(*args, **kwargs): # real signature unknown
    """ Same as a % b. """
    pass

def mul(*args, **kwargs): # real signature unknown
    """ Same as a * b. """
    pass

def ne(*args, **kwargs): # real signature unknown
    """ Same as a != b. """
    pass

def neg(*args, **kwargs): # real signature unknown
    """ Same as -a. """
    pass

def not_(*args, **kwargs): # real signature unknown
    """ Same as not a. """
    pass

def or_(*args, **kwargs): # real signature unknown
    """ Same as a | b. """
    pass

def pos(*args, **kwargs): # real signature unknown
    """ Same as +a. """
    pass

def pow(*args, **kwargs): # real signature unknown
    """ Same as a ** b. """
    pass

def rshift(*args, **kwargs): # real signature unknown
    """ Same as a >> b. """
    pass

def setitem(*args, **kwargs): # real signature unknown
    """ Same as a[b] = c. """
    pass

def sub(*args, **kwargs): # real signature unknown
    """ Same as a - b. """
    pass

def truediv(*args, **kwargs): # real signature unknown
    """ Same as a / b. """
    pass

def truth(*args, **kwargs): # real signature unknown
    """ Return True if a is true, False otherwise. """
    pass

def xor(*args, **kwargs): # real signature unknown
    """ Same as a ^ b. """
    pass

def _compare_digest(*args, **kwargs): # real signature unknown
    """
    Return 'a == b'.
    
    This function uses an approach designed to prevent
    timing analysis, making it appropriate for cryptography.
    
    a and b must both be of the same type: either str (ASCII only),
    or any bytes-like object.
    
    Note: If a and b are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of a and b--but not their values.
    """
    pass

# classes

class attrgetter(object):
    """
    Return a callable object that fetches the given attribute(s) from its operand.
    After f = attrgetter('name'), the call f(r) returns r.name.
    After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
    After h = attrgetter('name.first', 'name.last'), the call h(r) returns
    (r.name.first, r.name.last).
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __vectorcalloffset__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class itemgetter(object):
    """
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __vectorcalloffset__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class methodcaller(object):
    """
    Return a callable object that calls the given method on its operand.
    After f = methodcaller('name'), the call f(r) returns r.name().
    After g = methodcaller('name', 'date', foo=1), the call g(r) returns
    r.name('date', foo=1).
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7eeffdf5ef20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7eeffdf5efc0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7eeffdf5f060>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7eeffdf5f1a0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7eeffdf5f2e0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7eeffdf5f420>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7eeffdf5e2a0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_operator', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

