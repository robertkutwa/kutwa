# encoding: utf-8
# module _io
# from (built-in)
# by generator 1.147
"""
The io module provides the Python interfaces to stream handling. The
builtin open function is defined in this module.

At the top of the I/O hierarchy is the abstract base class IOBase. It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are
allowed to raise an OSError if they do not support a given operation.

Extending IOBase is RawIOBase which deals simply with the reading and
writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide
an interface to OS files.

BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its
subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer
streams that are readable, writable, and both respectively.
BufferedRandom provides a buffered interface to random access
streams. BytesIO is a simple stream of in-memory bytes.

Another IOBase subclass, TextIOBase, deals with the encoding and decoding
of streams into text. TextIOWrapper, which extends it, is a buffered text
interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO
is an in-memory stream for text.

Argument names are not part of the specification, and only the arguments
of open() are intended to be used as keyword arguments.

data:

DEFAULT_BUFFER_SIZE

   An int containing the default buffer size used by the module's buffered
   I/O classes. open() uses the file's blksize (as obtained by os.stat) if
   possible.
"""
# no imports

# Variables with simple values

DEFAULT_BUFFER_SIZE = 8192

# functions

def open(name, mode=None, buffering=None): # known case of _io.open
    """
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getencoding() is called to get the current locale encoding.
    (For reading and writing raw bytes use binary mode and leave encoding
    unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
    """
    return file('/dev/null')

def open_code(*args, **kwargs): # real signature unknown
    """
    Opens the provided file with the intent to import the contents.
    
    This may perform extra validation beyond open(), but is otherwise interchangeable
    with calling open(path, 'rb').
    """
    pass

def text_encoding(*args, **kwargs): # real signature unknown
    """
    A helper function to choose the text encoding.
    
    When encoding is not None, this function returns it.
    Otherwise, this function returns the default text encoding
    (i.e. "locale" or "utf-8" depends on UTF-8 mode).
    
    This function emits an EncodingWarning if encoding is None and
    sys.flags.warn_default_encoding is true.
    
    This can be used in APIs with an encoding=None parameter.
    However, please consider using encoding="utf-8" for new APIs.
    """
    pass

# classes

class BlockingIOError(OSError):
    """ I/O operation would block. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class _IOBase(object):
    """
    The abstract base class for all I/O classes.
    
    This class provides dummy implementations for many methods that
    derived classes can override selectively; the default implementations
    represent a file that cannot be read, written or seeked.
    
    Even though IOBase does not declare read, readinto, or write because
    their signatures will vary, implementations and clients should
    consider those methods part of the interface. Also, implementations
    may raise UnsupportedOperation when operations they do not support are
    called.
    
    The basic type used for binary data read from or written to a file is
    bytes. Other bytes-like objects are accepted as method arguments too.
    In some cases (such as readinto), a writable object is required. Text
    I/O classes work with str data.
    
    Note that calling any method (except additional calls to close(),
    which are ignored) on a closed stream should raise a ValueError.
    
    IOBase (and its subclasses) support the iterator protocol, meaning
    that an IOBase object can be iterated over yielding the lines in a
    stream.
    
    IOBase also supports the :keyword:`with` statement. In this example,
    fp is closed after the suite of the with statement is complete:
    
    with open('spam.txt', 'r') as fp:
        fp.write('Spam and eggs!')
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        Flush and close the IO object.
        
        This method has no effect if the file is already closed.
        """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """
        Return underlying file descriptor if one exists.
        
        Raise OSError if the IO object does not use a file descriptor.
        """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """
        Flush write buffers, if applicable.
        
        This is not implemented for read-only and non-blocking streams.
        """
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        """
        Return whether this is an 'interactive' stream.
        
        Return False if it can't be determined.
        """
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        """
        Return whether object was opened for reading.
        
        If False, read() will raise OSError.
        """
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        """
        Read and return a line from the stream.
        
        If size is specified, at most size bytes will be read.
        
        The line terminator is always b'\n' for binary files; for text
        files, the newlines argument to open can be used to select the line
        terminator(s) recognized.
        """
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of lines from the stream.
        
        hint can be specified to control the number of lines read: no more
        lines will be read if the total size (in bytes/characters) of all
        lines so far exceeds hint.
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Change the stream position to the given byte offset.
        
          offset
            The stream position, relative to 'whence'.
          whence
            The relative position to seek from.
        
        The offset is interpreted relative to the position indicated by whence.
        Values for whence are:
        
        * os.SEEK_SET or 0 -- start of stream (the default); offset should be zero or positive
        * os.SEEK_CUR or 1 -- current stream position; offset may be negative
        * os.SEEK_END or 2 -- end of stream; offset is usually negative
        
        Return the new absolute position.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        """
        Return whether object supports random access.
        
        If False, seek(), tell() and truncate() will raise OSError.
        This method may need to do a test seek().
        """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """ Return current stream position. """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """
        Truncate file to size bytes.
        
        File pointer is left unchanged. Size defaults to the current IO position
        as reported by tell(). Return the new size.
        """
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        """
        Return whether object was opened for writing.
        
        If False, write() will raise OSError.
        """
        pass

    def writelines(self, *args, **kwargs): # real signature unknown
        """
        Write a list of lines to stream.
        
        Line separators are not added, so it is usual for each of the
        lines provided to have a line separator at the end.
        """
        pass

    def _checkClosed(self, *args, **kwargs): # real signature unknown
        pass

    def _checkReadable(self, *args, **kwargs): # real signature unknown
        pass

    def _checkSeekable(self, *args, **kwargs): # real signature unknown
        pass

    def _checkWritable(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __enter__(self, *args, **kwargs): # real signature unknown
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'__iter__\': <slot wrapper \'__iter__\' of \'_io._IOBase\' objects>, \'__next__\': <slot wrapper \'__next__\' of \'_io._IOBase\' objects>, \'__del__\': <slot wrapper \'__del__\' of \'_io._IOBase\' objects>, \'seek\': <method \'seek\' of \'_io._IOBase\' objects>, \'tell\': <method \'tell\' of \'_io._IOBase\' objects>, \'truncate\': <method \'truncate\' of \'_io._IOBase\' objects>, \'flush\': <method \'flush\' of \'_io._IOBase\' objects>, \'close\': <method \'close\' of \'_io._IOBase\' objects>, \'seekable\': <method \'seekable\' of \'_io._IOBase\' objects>, \'readable\': <method \'readable\' of \'_io._IOBase\' objects>, \'writable\': <method \'writable\' of \'_io._IOBase\' objects>, \'_checkClosed\': <method \'_checkClosed\' of \'_io._IOBase\' objects>, \'_checkSeekable\': <method \'_checkSeekable\' of \'_io._IOBase\' objects>, \'_checkReadable\': <method \'_checkReadable\' of \'_io._IOBase\' objects>, \'_checkWritable\': <method \'_checkWritable\' of \'_io._IOBase\' objects>, \'fileno\': <method \'fileno\' of \'_io._IOBase\' objects>, \'isatty\': <method \'isatty\' of \'_io._IOBase\' objects>, \'__enter__\': <method \'__enter__\' of \'_io._IOBase\' objects>, \'__exit__\': <method \'__exit__\' of \'_io._IOBase\' objects>, \'readline\': <method \'readline\' of \'_io._IOBase\' objects>, \'readlines\': <method \'readlines\' of \'_io._IOBase\' objects>, \'writelines\': <method \'writelines\' of \'_io._IOBase\' objects>, \'__dict__\': <attribute \'__dict__\' of \'_io._IOBase\' objects>, \'closed\': <attribute \'closed\' of \'_io._IOBase\' objects>, \'__doc__\': "The abstract base class for all I/O classes.\\n\\nThis class provides dummy implementations for many methods that\\nderived classes can override selectively; the default implementations\\nrepresent a file that cannot be read, written or seeked.\\n\\nEven though IOBase does not declare read, readinto, or write because\\ntheir signatures will vary, implementations and clients should\\nconsider those methods part of the interface. Also, implementations\\nmay raise UnsupportedOperation when operations they do not support are\\ncalled.\\n\\nThe basic type used for binary data read from or written to a file is\\nbytes. Other bytes-like objects are accepted as method arguments too.\\nIn some cases (such as readinto), a writable object is required. Text\\nI/O classes work with str data.\\n\\nNote that calling any method (except additional calls to close(),\\nwhich are ignored) on a closed stream should raise a ValueError.\\n\\nIOBase (and its subclasses) support the iterator protocol, meaning\\nthat an IOBase object can be iterated over yielding the lines in a\\nstream.\\n\\nIOBase also supports the :keyword:`with` statement. In this example,\\nfp is closed after the suite of the with statement is complete:\\n\\nwith open(\'spam.txt\', \'r\') as fp:\\n    fp.write(\'Spam and eggs!\')\\n", \'__module__\': \'_io\'})'


class _BufferedIOBase(_IOBase):
    """
    Base class for buffered IO objects.
    
    The main difference with RawIOBase is that the read() method
    supports omitting the size argument, and does not have a default
    implementation that defers to readinto().
    
    In addition, read(), readinto() and write() may raise
    BlockingIOError if the underlying raw stream is in non-blocking
    mode and not ready; unlike their raw counterparts, they will never
    return None.
    
    A typical implementation should not inherit from a RawIOBase
    implementation, but wrap one.
    """
    def detach(self, *args, **kwargs): # real signature unknown
        """
        Disconnect this buffer from its underlying raw stream and return it.
        
        After the raw stream has been detached, the buffer is in an unusable
        state.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read and return up to n bytes.
        
        If the size argument is omitted, None, or negative, read and
        return all data until EOF.
        
        If the size argument is positive, and the underlying raw stream is
        not 'interactive', multiple raw reads may be issued to satisfy
        the byte count (unless EOF is reached first).
        However, for interactive raw streams (as well as sockets and pipes),
        at most one raw read will be issued, and a short result does not
        imply that EOF is imminent.
        
        Return an empty bytes object on EOF.
        
        Return None if the underlying raw stream was open in non-blocking
        mode and no data is available at the moment.
        """
        pass

    def read1(self, *args, **kwargs): # real signature unknown
        """
        Read and return up to size bytes, with at most one read() call to the underlying raw stream.
        
        Return an empty bytes object on EOF.
        A short result does not imply that EOF is imminent.
        """
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def readinto1(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write buffer b to the IO stream.
        
        Return the number of bytes written, which is always
        the length of b in bytes.
        
        Raise BlockingIOError if the buffer is full and the
        underlying raw stream cannot accept more data at the moment.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class BufferedRandom(_BufferedIOBase):
    """
    A buffered interface to random access streams.
    
    The constructor creates a reader and writer for a seekable stream,
    raw, given in the first argument. If the buffer_size is omitted it
    defaults to DEFAULT_BUFFER_SIZE.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def read1(self, *args, **kwargs): # real signature unknown
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def readinto1(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def _dealloc_warn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finalizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BufferedReader(_BufferedIOBase):
    """ Create a new buffered reader using the given readable raw IO object. """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def read1(self, *args, **kwargs): # real signature unknown
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def readinto1(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        pass

    def _dealloc_warn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finalizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BufferedRWPair(_BufferedIOBase):
    """
    A buffered reader and writer object together.
    
    A buffered reader object and buffered writer object put together to
    form a sequential IO object that can read and write. This is typically
    used with a socket or two-way pipe.
    
    reader and writer are RawIOBase objects that are readable and
    writeable respectively. If the buffer_size is omitted it defaults to
    DEFAULT_BUFFER_SIZE.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def read1(self, *args, **kwargs): # real signature unknown
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def readinto1(self, *args, **kwargs): # real signature unknown
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BufferedWriter(_BufferedIOBase):
    """
    A buffer for a writeable sequential RawIO object.
    
    The constructor creates a BufferedWriter for the given writeable raw
    stream. If the buffer_size is not given, it defaults to
    DEFAULT_BUFFER_SIZE.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def _dealloc_warn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    raw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finalizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BytesIO(_BufferedIOBase):
    """ Buffered I/O implementation using an in-memory bytes buffer. """
    def close(self, *args, **kwargs): # real signature unknown
        """ Disable all I/O operations. """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """ Does nothing. """
        pass

    def getbuffer(self, *args, **kwargs): # real signature unknown
        """ Get a read-write view over the contents of the BytesIO object. """
        pass

    def getvalue(self, *args, **kwargs): # real signature unknown
        """ Retrieve the entire contents of the BytesIO object. """
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        """
        Always returns False.
        
        BytesIO objects are not connected to a TTY-like device.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read at most size bytes, returned as a bytes object.
        
        If the size argument is negative, read until EOF is reached.
        Return an empty bytes object at EOF.
        """
        pass

    def read1(self, *args, **kwargs): # real signature unknown
        """
        Read at most size bytes, returned as a bytes object.
        
        If the size argument is negative or omitted, read until EOF is reached.
        Return an empty bytes object at EOF.
        """
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be read. """
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        """
        Read bytes into buffer.
        
        Returns number of bytes read (0 for EOF), or None if the object
        is set not to block and has no data to read.
        """
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        """
        Next line from the file, as a bytes object.
        
        Retain newline.  A non-negative size argument limits the maximum
        number of bytes to return (an incomplete line may be returned then).
        Return an empty bytes object at EOF.
        """
        pass

    def readlines(self, *args, **kwargs): # real signature unknown
        """
        List of bytes objects, each a line from the file.
        
        Call readline() repeatedly and return a list of the lines so read.
        The optional size argument, if given, is an approximate bound on the
        total number of bytes in the lines returned.
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Change stream position.
        
        Seek to byte offset pos relative to position indicated by whence:
             0  Start of stream (the default).  pos should be >= 0;
             1  Current position - pos may be negative;
             2  End of stream - pos usually negative.
        Returns the new absolute position.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be seeked. """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """ Current file position, an integer. """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """
        Truncate the file to at most size bytes.
        
        Size defaults to the current file position, as returned by tell().
        The current file position is unchanged.  Returns the new size.
        """
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be written. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write bytes to file.
        
        Return the number of bytes written.
        """
        pass

    def writelines(self, *args, **kwargs): # real signature unknown
        """
        Write lines to the file.
        
        Note that newlines are not added.  lines can be any iterable object
        producing bytes-like objects. This is equivalent to calling write() for
        each element.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed."""



class _RawIOBase(_IOBase):
    """ Base class for raw binary I/O. """
    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readall(self, *args, **kwargs): # real signature unknown
        """ Read until EOF, using multiple read() call. """
        pass

    def readinto(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class FileIO(_RawIOBase):
    """
    Open a file.
    
    The mode can be 'r' (default), 'w', 'x' or 'a' for reading,
    writing, exclusive creation or appending.  The file will be created if it
    doesn't exist when opened for writing or appending; it will be truncated
    when opened for writing.  A FileExistsError will be raised if it already
    exists when opened for creating. Opening a file for creating implies
    writing so this mode behaves in a similar way to 'w'.Add a '+' to the mode
    to allow simultaneous reading and writing. A custom opener can be used by
    passing a callable as *opener*. The underlying file descriptor for the file
    object is then obtained by calling opener with (*name*, *flags*).
    *opener* must return an open file descriptor (passing os.open as *opener*
    results in functionality similar to passing None).
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        Close the file.
        
        A closed file cannot be used for further I/O operations.  close() may be
        called more than once without error.
        """
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        """ Return the underlying file descriptor (an integer). """
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        """ True if the file is connected to a TTY device. """
        pass

    def read(self, size=-1): # known case of _io.FileIO.read
        """
        Read at most size bytes, returned as bytes.
        
        Only makes one system call, so less data may be returned than requested.
        In non-blocking mode, returns None if no data is available.
        Return an empty bytes object at EOF.
        """
        return ""

    def readable(self, *args, **kwargs): # real signature unknown
        """ True if file was opened in a read mode. """
        pass

    def readall(self, *args, **kwargs): # real signature unknown
        """
        Read all data from the file, returned as bytes.
        
        In non-blocking mode, returns as much as is immediately available,
        or None if no data is available.  Return an empty bytes object at EOF.
        """
        pass

    def readinto(self): # real signature unknown; restored from __doc__
        """ Same as RawIOBase.readinto(). """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Move to new file position and return the file position.
        
        Argument offset is a byte count.  Optional argument whence defaults to
        SEEK_SET or 0 (offset from start of file, offset should be >= 0); other values
        are SEEK_CUR or 1 (move relative to current position, positive or negative),
        and SEEK_END or 2 (move relative to end of file, usually negative, although
        many platforms allow seeking beyond the end of a file).
        
        Note that not all file objects are seekable.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        """ True if file supports random-access. """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """
        Current file position.
        
        Can raise OSError for non seekable files.
        """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """
        Truncate the file to at most size bytes and return the truncated size.
        
        Size defaults to the current file position, as returned by tell().
        The current file position is changed to the value of size.
        """
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        """ True if file was opened in a write mode. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write buffer b to file, return number of bytes written.
        
        Only makes one system call, so not all of the data may be written.
        The number of bytes actually written is returned.  In non-blocking mode,
        returns None if the write would block.
        """
        pass

    def _dealloc_warn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed"""

    closefd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file descriptor will be closed by close()."""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String giving the file mode"""

    _blksize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finalizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IncrementalNewlineDecoder(object):
    """
    Codec used when reading a file in universal newlines mode.
    
    It wraps another incremental decoder, translating \r\n and \r into \n.
    It also records the types of newlines encountered.  When used with
    translate=False, it ensures that the newline sequence is returned in
    one piece. When used with decoder=None, it expects unicode strings as
    decode input and translates newlines without first invoking an external
    decoder.
    """
    def decode(self, *args, **kwargs): # real signature unknown
        pass

    def getstate(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setstate(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _TextIOBase(_IOBase):
    """
    Base class for text I/O.
    
    This class provides a character and line based interface to stream
    I/O. There is no readinto method because Python's character strings
    are immutable.
    """
    def detach(self, *args, **kwargs): # real signature unknown
        """
        Separate the underlying buffer from the TextIOBase and return it.
        
        After the underlying buffer has been detached, the TextIO is in an unusable state.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read at most size characters from stream.
        
        Read from underlying buffer until we have size characters or we hit EOF.
        If size is negative or omitted, read until EOF.
        """
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        """
        Read until newline or EOF.
        
        Return an empty string if EOF is hit immediately.
        If size is specified, at most size characters will be read.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write string s to stream.
        
        Return the number of characters written
        (which is always equal to the length of the string).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoding of the text stream.

Subclasses should override.
"""

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The error setting of the decoder or encoder.

Subclasses should override.
"""

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line endings translated so far.

Only line endings translated during reading are considered.

Subclasses should override.
"""



class StringIO(_TextIOBase):
    """
    Text I/O implementation using an in-memory buffer.
    
    The initial_value argument sets the value of object.  The newline
    argument is like the one of TextIOWrapper's constructor.
    """
    def close(self, *args, **kwargs): # real signature unknown
        """
        Close the IO object.
        
        Attempting any further operation after the object is closed
        will raise a ValueError.
        
        This method has no effect if the file is already closed.
        """
        pass

    def getvalue(self, *args, **kwargs): # real signature unknown
        """ Retrieve the entire contents of the object. """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read at most size characters, returned as a string.
        
        If the argument is negative or omitted, read until EOF
        is reached. Return an empty string at EOF.
        """
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be read. """
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        """
        Read until newline or EOF.
        
        Returns an empty string if EOF is hit immediately.
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        """
        Change stream position.
        
        Seek to character offset pos relative to position indicated by whence:
            0  Start of stream (the default).  pos should be >= 0;
            1  Current position - pos must be 0;
            2  End of stream - pos must be 0.
        Returns the new absolute position.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be seeked. """
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        """ Tell the current file position. """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        """
        Truncate size to pos.
        
        The pos argument defaults to the current file position, as
        returned by tell().  The current file position is unchanged.
        Returns the new absolute position.
        """
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        """ Returns True if the IO object can be written. """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Write string to file.
        
        Returns the number of characters written, which is always equal to
        the length of the string.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class TextIOWrapper(_TextIOBase):
    """
    Character and line based layer over a BufferedIOBase object, buffer.
    
    encoding gives the name of the encoding that the stream will be
    decoded or encoded with. It defaults to locale.getencoding().
    
    errors determines the strictness of encoding and decoding (see
    help(codecs.Codec) or the documentation for codecs.register) and
    defaults to "strict".
    
    newline controls how line endings are handled. It can be None, '',
    '\n', '\r', and '\r\n'.  It works as follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If line_buffering is True, a call to flush is implied when a call to
    write contains a newline character.
    """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        pass

    def readline(self, *args, **kwargs): # real signature unknown
        pass

    def reconfigure(self, *args, **kwargs): # real signature unknown
        """
        Reconfigure the text stream with new parameters.
        
        This also does an implicit stream flush.
        """
        pass

    def seek(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Set the stream position, and return the new stream position.
        
          cookie
            Zero or an opaque number returned by tell().
          whence
            The relative position to seek from.
        
        Four operations are supported, given by the following argument
        combinations:
        
        - seek(0, SEEK_SET): Rewind to the start of the stream.
        - seek(cookie, SEEK_SET): Restore a previous position;
          'cookie' must be a number returned by tell().
        - seek(0, SEEK_END): Fast-forward to the end of the stream.
        - seek(0, SEEK_CUR): Leave the current stream position unchanged.
        
        Any other argument combinations are invalid,
        and may raise exceptions.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """
        Return the stream position as an opaque number.
        
        The return value of tell() can be given as input to seek(), to restore a
        previous stream position.
        """
        pass

    def truncate(self, *args, **kwargs): # real signature unknown
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_through = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _CHUNK_SIZE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finalizing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnsupportedOperation(OSError, ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class _BytesIOBuffer(object):
    # no doc
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
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

__spec__ = None # (!) real value is "ModuleSpec(name='_io', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

