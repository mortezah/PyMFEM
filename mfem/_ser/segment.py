# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_segment')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_segment')
    _segment = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_segment', [dirname(__file__)])
        except ImportError:
            import _segment
            return _segment
        try:
            _mod = imp.load_module('_segment', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _segment = swig_import_helper()
    del swig_import_helper
else:
    import _segment
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import mfem._ser.element
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.densemat
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.geom
import mfem._ser.intrules
import mfem._ser.table
import mfem._ser.hash
class Segment(mfem._ser.element.Element):
    """Proxy of C++ mfem::Segment class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.element.Element]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Segment, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.element.Element]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Segment, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::Segment self) -> Segment
        __init__(mfem::Segment self, int const * ind, int attr=1) -> Segment
        __init__(mfem::Segment self, int const * ind) -> Segment
        __init__(mfem::Segment self, int ind1, int ind2, int attr=1) -> Segment
        __init__(mfem::Segment self, int ind1, int ind2) -> Segment
        """
        this = _segment.new_Segment(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetVertices(self, ind):
        """SetVertices(Segment self, int const * ind)"""
        return _segment.Segment_SetVertices(self, ind)


    def GetType(self):
        """GetType(Segment self) -> mfem::Element::Type"""
        return _segment.Segment_GetType(self)


    def GetVertices(self, *args):
        """
        GetVertices(Segment self, intArray v)
        GetVertices(Segment self) -> int *
        """
        return _segment.Segment_GetVertices(self, *args)


    def GetNVertices(self):
        """GetNVertices(Segment self) -> int"""
        return _segment.Segment_GetNVertices(self)


    def GetNEdges(self):
        """GetNEdges(Segment self) -> int"""
        return _segment.Segment_GetNEdges(self)


    def GetEdgeVertices(self, ei):
        """GetEdgeVertices(Segment self, int ei) -> int const *"""
        return _segment.Segment_GetEdgeVertices(self, ei)


    def GetNFaces(self, nFaceVertices):
        """GetNFaces(Segment self, int & nFaceVertices) -> int"""
        return _segment.Segment_GetNFaces(self, nFaceVertices)


    def GetFaceVertices(self, fi):
        """GetFaceVertices(Segment self, int fi) -> int const *"""
        return _segment.Segment_GetFaceVertices(self, fi)


    def Duplicate(self, m):
        """Duplicate(Segment self, mfem::Mesh * m) -> Element"""
        return _segment.Segment_Duplicate(self, m)

    __swig_destroy__ = _segment.delete_Segment
    __del__ = lambda self: None
Segment_swigregister = _segment.Segment_swigregister
Segment_swigregister(Segment)

# This file is compatible with both classic and new-style classes.

cvar = _segment.cvar

