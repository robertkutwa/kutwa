# encoding: utf-8
# module select
# from (built-in)
# by generator 1.147
"""
This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows, only sockets are supported; on Unix, all file descriptors.
"""
# no imports

# Variables with simple values

EPOLLERR = 8
EPOLLET = 2147483648
EPOLLEXCLUSIVE = 268435456
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDHUP = 8192
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256

EPOLL_CLOEXEC = 524288

PIPE_BUF = 4096

POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDHUP = 8192
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256

# functions

def poll(*args, **kwargs): # real signature unknown
    """
    Returns a polling object.
    
    This object supports registering and unregistering file descriptors, and then
    polling them for I/O events.
    """
    pass

def select(*args, **kwargs): # real signature unknown
    """
    Wait until one or more file descriptors are ready for some kind of I/O.
    
    The first three arguments are iterables of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an "exceptional condition"
    If only one kind of condition is required, pass [] for the other lists.
    
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows, only sockets are supported; on Unix, all file
    descriptors can be used.
    """
    pass

# classes

class epoll(object):
    """
    select.epoll(sizehint=-1, flags=0)
    
    Returns an epolling object
    
    sizehint must be a positive integer or -1 for the default size. The
    sizehint is used to optimize internal data structures. It doesn't limit
    the maximum number of monitored events.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the epoll control file descriptor.
        
        Further operations on the epoll object will raise an exception.
        """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ Return the epoll control file descriptor. """
        pass

    @classmethod
    def fromfd(cls, *args, **kwargs): # real signature unknown
        """ Create an epoll object from a given control fd. """
        pass

    def modify(self, *args, **kwargs): # real signature unknown
        """
        Modify event mask for a registered file descriptor.
        
          fd
            the target file descriptor of the operation
          eventmask
            a bit set composed of the various EPOLL constants
        """
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        """
        Wait for events on the epoll file descriptor.
        
          timeout
            the maximum time to wait in seconds (as float);
            a timeout of None or -1 makes poll wait indefinitely
          maxevents
            the maximum number of events returned; -1 means no limit
        
        Returns a list containing any descriptors that have events to report,
        as a list of (fd, events) 2-tuples.
        """
        pass

    def register(self, *args, **kwargs): # real signature unknown
        """
        Registers a new fd or raises an OSError if the fd is already registered.
        
          fd
            the target file descriptor of the operation
          eventmask
            a bit set composed of the various EPOLL constants
        
        The epoll interface supports all file descriptors that support poll.
        """
        pass

    def unregister(self, *args, **kwargs): # real signature unknown
        """
        Remove a registered file descriptor from the epoll object.
        
          fd
            the target file descriptor of the operation
        """
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, sizehint=-1, flags=0): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the epoll handler is closed"""



class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""



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

__spec__ = None # (!) real value is "ModuleSpec(name='select', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

