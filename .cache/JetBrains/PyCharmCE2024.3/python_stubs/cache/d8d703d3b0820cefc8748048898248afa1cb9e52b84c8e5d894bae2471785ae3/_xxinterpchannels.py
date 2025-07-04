# encoding: utf-8
# module _xxinterpchannels
# from /usr/lib/python3.12/lib-dynload/_xxinterpchannels.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""
# no imports

# functions

def close(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_close(cid, *, send=None, recv=None, force=False)
    
    Close the channel for all interpreters.
    
    If the channel is empty then the keyword args are ignored and both
    ends are immediately closed.  Otherwise, if 'force' is True then
    all queued items are released and both ends are immediately
    closed.
    
    If the channel is not empty *and* 'force' is False then following
    happens:
    
     * recv is True (regardless of send):
       - raise ChannelNotEmptyError
     * recv is None and send is None:
       - raise ChannelNotEmptyError
     * send is True and recv is not True:
       - fully close the 'send' end
       - close the 'recv' end to interpreters not already receiving
       - fully close it once empty
    
    Closing an already closed channel results in a ChannelClosedError.
    
    Once the channel's ID has no more ref counts in any interpreter
    the channel will be destroyed.
    """
    pass

def create(): # real signature unknown; restored from __doc__
    """
    channel_create() -> cid
    
    Create a new cross-interpreter channel and return a unique generated ID.
    """
    pass

def destroy(cid): # real signature unknown; restored from __doc__
    """
    channel_destroy(cid)
    
    Close and finalize the channel.  Afterward attempts to use the channel
    will behave as though it never existed.
    """
    pass

def list_all(): # real signature unknown; restored from __doc__
    """
    channel_list_all() -> [cid]
    
    Return the list of all IDs for active channels.
    """
    pass

def list_interpreters(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_list_interpreters(cid, *, send) -> [id]
    
    Return the list of all interpreter IDs associated with an end of the channel.
    
    The 'send' argument should be a boolean indicating whether to use the send or
    receive end.
    """
    pass

def recv(cid, default=None): # real signature unknown; restored from __doc__
    """
    channel_recv(cid, [default]) -> obj
    
    Return a new object from the data at the front of the channel's queue.
    
    If there is nothing to receive then raise ChannelEmptyError, unless
    a default value is provided.  In that case return it.
    """
    pass

def release(cid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    channel_release(cid, *, send=None, recv=None, force=True)
    
    Close the channel for the current interpreter.  'send' and 'recv'
    (bool) may be used to indicate the ends to close.  By default both
    ends are closed.  Closing an already closed end is a noop.
    """
    pass

def send(cid, obj): # real signature unknown; restored from __doc__
    """
    channel_send(cid, obj)
    
    Add the object's data to the channel's queue.
    """
    pass

def _channel_id(*args, **kwargs): # real signature unknown
    pass

# classes

class ChannelError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class ChannelClosedError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelEmptyError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelID(object):
    """ A channel ID identifies a channel and may be used as an int. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """'send', 'recv', or 'both'"""

    recv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the 'recv' end of the channel"""

    send = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the 'send' end of the channel"""



class ChannelNotEmptyError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ChannelNotFoundError(ChannelError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7eeffd44e210>'

__spec__ = None # (!) real value is "ModuleSpec(name='_xxinterpchannels', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7eeffd44e210>, origin='/usr/lib/python3.12/lib-dynload/_xxinterpchannels.cpython-312-x86_64-linux-gnu.so')"

