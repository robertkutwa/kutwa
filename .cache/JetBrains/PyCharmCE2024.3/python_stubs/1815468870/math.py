# encoding: utf-8
# module math
# from (built-in)
# by generator 1.147
"""
This module provides access to the mathematical functions
defined by the C standard.
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
    """
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.
    """
    pass

def acosh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic cosine of x. """
    pass

def asin(*args, **kwargs): # real signature unknown
    """
    Return the arc sine (measured in radians) of x.
    
    The result is between -pi/2 and pi/2.
    """
    pass

def asinh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic sine of x. """
    pass

def atan(*args, **kwargs): # real signature unknown
    """
    Return the arc tangent (measured in radians) of x.
    
    The result is between -pi/2 and pi/2.
    """
    pass

def atan2(*args, **kwargs): # real signature unknown
    """
    Return the arc tangent (measured in radians) of y/x.
    
    Unlike atan(y/x), the signs of both x and y are considered.
    """
    pass

def atanh(*args, **kwargs): # real signature unknown
    """ Return the inverse hyperbolic tangent of x. """
    pass

def cbrt(*args, **kwargs): # real signature unknown
    """ Return the cube root of x. """
    pass

def ceil(*args, **kwargs): # real signature unknown
    """
    Return the ceiling of x as an Integral.
    
    This is the smallest integer >= x.
    """
    pass

def comb(*args, **kwargs): # real signature unknown
    """
    Number of ways to choose k items from n items without repetition and without order.
    
    Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
    to zero when k > n.
    
    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of the
    expression (1 + x)**n.
    
    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.
    """
    pass

def copysign(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return a float with the magnitude (absolute value) of x but the sign of y.
    
    On platforms that support signed zeros, copysign(1.0, -0.0)
    returns -1.0.
    """
    pass

def cos(*args, **kwargs): # real signature unknown
    """ Return the cosine of x (measured in radians). """
    pass

def cosh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic cosine of x. """
    pass

def degrees(*args, **kwargs): # real signature unknown
    """ Convert angle x from radians to degrees. """
    pass

def dist(*args, **kwargs): # real signature unknown
    """
    Return the Euclidean distance between two points p and q.
    
    The points should be specified as sequences (or iterables) of
    coordinates.  Both inputs must have the same dimension.
    
    Roughly equivalent to:
        sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    """
    pass

def erf(*args, **kwargs): # real signature unknown
    """ Error function at x. """
    pass

def erfc(*args, **kwargs): # real signature unknown
    """ Complementary error function at x. """
    pass

def exp(*args, **kwargs): # real signature unknown
    """ Return e raised to the power of x. """
    pass

def exp2(*args, **kwargs): # real signature unknown
    """ Return 2 raised to the power of x. """
    pass

def expm1(*args, **kwargs): # real signature unknown
    """
    Return exp(x)-1.
    
    This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    """
    pass

def fabs(*args, **kwargs): # real signature unknown
    """ Return the absolute value of the float x. """
    pass

def factorial(*args, **kwargs): # real signature unknown
    """
    Find n!.
    
    Raise a ValueError if x is negative or non-integral.
    """
    pass

def floor(*args, **kwargs): # real signature unknown
    """
    Return the floor of x as an Integral.
    
    This is the largest integer <= x.
    """
    pass

def fmod(x, y): # real signature unknown; restored from __doc__
    """
    Return fmod(x, y), according to platform C.
    
    x % y may differ.
    """
    pass

def frexp(*args, **kwargs): # real signature unknown
    """
    Return the mantissa and exponent of x, as pair (m, e).
    
    m is a float and e is an int, such that x = m * 2.**e.
    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    """
    pass

def fsum(*args, **kwargs): # real signature unknown
    """
    Return an accurate floating point sum of values in the iterable seq.
    
    Assumes IEEE-754 floating point arithmetic.
    """
    pass

def gamma(*args, **kwargs): # real signature unknown
    """ Gamma function at x. """
    pass

def gcd(*args, **kwargs): # real signature unknown
    """ Greatest Common Divisor. """
    pass

def hypot(*coordinates): # real signature unknown; restored from __doc__
    """
    hypot(*coordinates) -> value
    
    Multidimensional Euclidean distance from the origin to a point.
    
    Roughly equivalent to:
        sqrt(sum(x**2 for x in coordinates))
    
    For a two dimensional point (x, y), gives the hypotenuse
    using the Pythagorean theorem:  sqrt(x*x + y*y).
    
    For example, the hypotenuse of a 3/4/5 right triangle is:
    
        >>> hypot(3.0, 4.0)
        5.0
    """
    pass

def isclose(*args, **kwargs): # real signature unknown
    """
    Determine whether two floating point numbers are close in value.
    
      rel_tol
        maximum difference for being considered "close", relative to the
        magnitude of the input values
      abs_tol
        maximum difference for being considered "close", regardless of the
        magnitude of the input values
    
    Return True if a is close in value to b, and False otherwise.
    
    For the values to be considered close, the difference between them
    must be smaller than at least one of the tolerances.
    
    -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
    is, NaN is not close to anything, even itself.  inf and -inf are
    only close to themselves.
    """
    pass

def isfinite(*args, **kwargs): # real signature unknown
    """ Return True if x is neither an infinity nor a NaN, and False otherwise. """
    pass

def isinf(*args, **kwargs): # real signature unknown
    """ Return True if x is a positive or negative infinity, and False otherwise. """
    pass

def isnan(*args, **kwargs): # real signature unknown
    """ Return True if x is a NaN (not a number), and False otherwise. """
    pass

def isqrt(*args, **kwargs): # real signature unknown
    """ Return the integer part of the square root of the input. """
    pass

def lcm(*args, **kwargs): # real signature unknown
    """ Least Common Multiple. """
    pass

def ldexp(*args, **kwargs): # real signature unknown
    """
    Return x * (2**i).
    
    This is essentially the inverse of frexp().
    """
    pass

def lgamma(*args, **kwargs): # real signature unknown
    """ Natural logarithm of absolute value of Gamma function at x. """
    pass

def log(x, base=None): # real signature unknown; restored from __doc__
    """
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base is not specified, returns the natural logarithm (base e) of x.
    """
    pass

def log10(*args, **kwargs): # real signature unknown
    """ Return the base 10 logarithm of x. """
    pass

def log1p(*args, **kwargs): # real signature unknown
    """
    Return the natural logarithm of 1+x (base e).
    
    The result is computed in a way which is accurate for x near zero.
    """
    pass

def log2(*args, **kwargs): # real signature unknown
    """ Return the base 2 logarithm of x. """
    pass

def modf(*args, **kwargs): # real signature unknown
    """
    Return the fractional and integer parts of x.
    
    Both results carry the sign of x and are floats.
    """
    pass

def nextafter(*args, **kwargs): # real signature unknown
    """
    Return the floating-point value the given number of steps after x towards y.
    
    If steps is not specified or is None, it defaults to 1.
    
    Raises a TypeError, if x or y is not a double, or if steps is not an integer.
    Raises ValueError if steps is negative.
    """
    pass

def perm(*args, **kwargs): # real signature unknown
    """
    Number of ways to choose k items from n items without repetition and with order.
    
    Evaluates to n! / (n - k)! when k <= n and evaluates
    to zero when k > n.
    
    If k is not specified or is None, then k defaults to n
    and the function returns n!.
    
    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.
    """
    pass

def pow(*args, **kwargs): # real signature unknown
    """ Return x**y (x to the power of y). """
    pass

def prod(*args, **kwargs): # real signature unknown
    """
    Calculate the product of all the elements in the input iterable.
    
    The default start value for the product is 1.
    
    When the iterable is empty, return the start value.  This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.
    """
    pass

def radians(*args, **kwargs): # real signature unknown
    """ Convert angle x from degrees to radians. """
    pass

def remainder(*args, **kwargs): # real signature unknown
    """
    Difference between x and the closest integer multiple of y.
    
    Return x - n*y where n*y is the closest integer multiple of y.
    In the case where x is exactly halfway between two multiples of
    y, the nearest even value of n is used. The result is always exact.
    """
    pass

def sin(*args, **kwargs): # real signature unknown
    """ Return the sine of x (measured in radians). """
    pass

def sinh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic sine of x. """
    pass

def sqrt(*args, **kwargs): # real signature unknown
    """ Return the square root of x. """
    pass

def sumprod(*args, **kwargs): # real signature unknown
    """
    Return the sum of products of values from two iterables p and q.
    
    Roughly equivalent to:
    
        sum(itertools.starmap(operator.mul, zip(p, q, strict=True)))
    
    For float and mixed int/float inputs, the intermediate products
    and sums are computed with extended precision.
    """
    pass

def tan(*args, **kwargs): # real signature unknown
    """ Return the tangent of x (measured in radians). """
    pass

def tanh(*args, **kwargs): # real signature unknown
    """ Return the hyperbolic tangent of x. """
    pass

def trunc(*args, **kwargs): # real signature unknown
    """
    Truncates the Real x to the nearest Integral toward 0.
    
    Uses the __trunc__ magic method.
    """
    pass

def ulp(*args, **kwargs): # real signature unknown
    """ Return the value of the least significant bit of the float x. """
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

__spec__ = None # (!) real value is "ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

