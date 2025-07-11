# encoding: utf-8
# module _zoneinfo
# from /usr/lib/python3.12/lib-dynload/_zoneinfo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
""" C implementation of the zoneinfo module """

# imports
import datetime as __datetime


# no functions
# classes

class ZoneInfo(__datetime.tzinfo):
    # no doc
    @classmethod
    def clear_cache(cls, *args, **kwargs): # real signature unknown
        pass

    def dst(self, *args, **kwargs): # real signature unknown
        """ Retrieve a timedelta representing the amount of DST applied in a zone at the given datetime. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ Given a datetime with local time in UTC, retrieve an adjusted datetime in local time. """
        pass

    @classmethod
    def from_file(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def no_cache(cls, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ Retrieve a string containing the abbreviation for the time zone that applies in a zone at a given datetime. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Retrieve a timedelta representing the UTC offset in a zone at the given datetime. """
        pass

    @classmethod
    def _unpickle(cls, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    @classmethod
    def __init_subclass__(cls, *args, **kwargs): # real signature unknown
        """ Function to initialize subclasses. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Function for serialization with the pickle protocol. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7eeffd44d8b0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_zoneinfo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7eeffd44d8b0>, origin='/usr/lib/python3.12/lib-dynload/_zoneinfo.cpython-312-x86_64-linux-gnu.so')"

