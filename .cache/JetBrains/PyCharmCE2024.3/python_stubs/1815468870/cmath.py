# encoding: utf-8
# module cmath
# from (built-in)
# by generator 1.147
"""
This module provides access to mathematical functions for complex
numbers.
"""
# no imports

# Variables with simple values
e = 2.718281828459045

inf = inf

nan = nan

pi = 3.141592653589793

tau = 6.283185307179586

# functions

def acos(*args, **kwargs): # real signature unknown
    """ Return the arc cosine of z. """
    pass

def acosh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic cosine of z. """
    pass

def asin(*args, **kwargs): # real signature unknown
    """ Return the arc sine of z. """
    pass

def asinh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic sine of z. """
    pass

def atan(*args, **kwargs): # real signature unknown
    """ Return the arc tangent of z. """
    pass

def atanh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic tangent of z. """
    pass

def cos(*args, **kwargs): # real signature unknown
    """ Return the cosine of z. """
    pass

def cosh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic cosine of z. """
    pass

def exp(*args, **kwargs): # real signature unknown
    """ Return the exponential value e**z. """
    pass

def isclose(*args, **kwargs): # real signature unknown
    """
    Determine whether two complex numbers are close in value.
    
      rel_tol
        maximum difference for being considered "close", relative to the
        magnitude of the input values
      abs_tol
        maximum difference for being considered "close", regardless of the
        magnitude of the input values
    
    Return True if a is close in value to b, and False otherwise.
    
    For the values to be considered close, the difference between them must be
    smaller than at least one of the tolerances.
    
    -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
    not close to anything, even itself. inf and -inf are only close to themselves.
    """
    pass

def isfinite(*args, **kwargs): # real signature unknown
    """ Return True if both the real and imaginary parts of z are finite, else False. """
    pass

def isinf(*args, **kwargs): # real signature unknown
    """ Checks if the real or imaginary part of z is infinite. """
    pass

def isnan(*args, **kwargs): # real signature unknown
    """ Checks if the real or imaginary part of z not a number (NaN). """
    pass

def log(z, base=None): # real signature unknown; restored from __doc__
    """
    log(z[, base]) -> the logarithm of z to the given base.
    
    If the base is not specified, returns the natural logarithm (base e) of z.
    """
    pass

def log10(*args, **kwargs): # real signature unknown
    """ Return the base-10 logarithm of z. """
    pass

def phase(*args, **kwargs): # real signature unknown
    """ Return argument, also known as the phase angle, of a complex. """
    pass

def polar(*args, **kwargs): # real signature unknown
    """
    Convert a complex from rectangular coordinates to polar coordinates.
    
    r is the distance from 0 and phi the phase angle.
    """
    pass

def rect(*args, **kwargs): # real signature unknown
    """ Convert from polar coordinates to rectangular coordinates. """
    pass

def sin(*args, **kwargs): # real signature unknown
    """ Return the sine of z. """
    pass

def sinh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic sine of z. """
    pass

def sqrt(*args, **kwargs): # real signature unknown
    """ Return the square root of z. """
    pass

def tan(*args, **kwargs): # real signature unknown
    """ Return the tangent of z. """
    pass

def tanh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic tangent of z. """
    pass

# classes

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

infj = None # (!) real value is 'infj'

nanj = None # (!) real value is 'nanj'

__spec__ = None # (!) real value is "ModuleSpec(name='cmath', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

