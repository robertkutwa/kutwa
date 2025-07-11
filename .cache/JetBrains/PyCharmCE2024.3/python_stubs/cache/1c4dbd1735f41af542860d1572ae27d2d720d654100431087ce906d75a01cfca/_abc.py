# encoding: utf-8
# module _abc
# from (built-in)
# by generator 1.147
""" Module contains faster C implementation of abc.ABCMeta """
# no imports

# functions

def get_cache_token(*args, **kwargs): # real signature unknown
    """
    Returns the current ABC cache token.
    
    The token is an opaque object (supporting equality testing) identifying the
    current version of the ABC cache for virtual subclasses. The token changes
    with every call to register() on any ABC.
    """
    pass

def _abc_init(*args, **kwargs): # real signature unknown
    """ Internal ABC helper for class set-up. Should be never used outside abc module. """
    pass

def _abc_instancecheck(*args, **kwargs): # real signature unknown
    """ Internal ABC helper for instance checks. Should be never used outside abc module. """
    pass

def _abc_register(*args, **kwargs): # real signature unknown
    """ Internal ABC helper for subclasss registration. Should be never used outside abc module. """
    pass

def _abc_subclasscheck(*args, **kwargs): # real signature unknown
    """ Internal ABC helper for subclasss checks. Should be never used outside abc module. """
    pass

def _get_dump(*args, **kwargs): # real signature unknown
    """
    Internal ABC helper for cache and registry debugging.
    
    Return shallow copies of registry, of both caches, and
    negative cache version. Don't call this function directly,
    instead use ABC._dump_registry() for a nice repr.
    """
    pass

def _reset_caches(*args, **kwargs): # real signature unknown
    """
    Internal ABC helper to reset both caches of a given class.
    
    Should be only used by refleak.py
    """
    pass

def _reset_registry(*args, **kwargs): # real signature unknown
    """
    Internal ABC helper to reset registry of a given class.
    
    Should be only used by refleak.py
    """
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

__spec__ = None # (!) real value is "ModuleSpec(name='_abc', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

