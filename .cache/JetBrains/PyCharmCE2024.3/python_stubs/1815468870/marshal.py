# encoding: utf-8
# module marshal
# from (built-in)
# by generator 1.147
"""
This module contains functions that can read and write Python values in
a binary format. The format is specific to Python, but independent of
machine architecture issues.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can be
written and read by this module. The following types are supported:
None, integers, floating point numbers, strings, bytes, bytearrays,
tuples, lists, sets, dictionaries, and code objects, where it
should be understood that tuples, lists and dictionaries are only
supported as long as the values contained therein are themselves
supported; and recursive lists and dictionaries should not be written
(they will cause infinite loops).

Variables:

version -- indicates the format that the module uses. Version 0 is the
    historical format, version 1 shares interned strings and version 2
    uses a binary format for floating point numbers.
    Version 3 shares common object references (New in version 3.4).

Functions:

dump() -- write value to a file
load() -- read value from a file
dumps() -- marshal value as a bytes object
loads() -- read value from a bytes-like object
"""
# no imports

# Variables with simple values

version = 4

# functions

def dump(*args, **kwargs): # real signature unknown
    """
    Write the value on the open file.
    
      value
        Must be a supported type.
      file
        Must be a writeable binary file.
      version
        Indicates the data format that dump should use.
    
    If the value has (or contains an object that has) an unsupported type, a
    ValueError exception is raised - but garbage data will also be written
    to the file. The object will not be properly read back by load().
    """
    pass

def dumps(*args, **kwargs): # real signature unknown
    """
    Return the bytes object that would be written to a file by dump(value, file).
    
      value
        Must be a supported type.
      version
        Indicates the data format that dumps should use.
    
    Raise a ValueError exception if value has (or contains an object that has) an
    unsupported type.
    """
    pass

def load(): # real signature unknown; restored from __doc__
    """
    Read one value from the open file and return it.
    
      file
        Must be readable binary file.
    
    If no valid value is read (e.g. because the data has a different Python
    version's incompatible marshal format), raise EOFError, ValueError or
    TypeError.
    
    Note: If an object containing an unsupported type was marshalled with
    dump(), load() will substitute None for the unmarshallable type.
    """
    pass

def loads(*args, **kwargs): # real signature unknown
    """
    Convert the bytes-like object to a value.
    
    If no valid value is found, raise EOFError, ValueError or TypeError.  Extra
    bytes in the input are ignored.
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

__spec__ = None # (!) real value is "ModuleSpec(name='marshal', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

