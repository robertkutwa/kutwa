# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.12/lib-dynload/_testcapi.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .object import object

class HeapCTypeWithDict(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    dictobj = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'dictobj': <member 'dictobj' of '_testcapi.HeapCTypeWithDict' objects>, '__dict__': <attribute '__dict__' of '_testcapi.HeapCTypeWithDict' objects>, '__doc__': None, '__module__': '_testcapi'})"


