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
        mname = '.'.join((pkg, '_hybridization')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_hybridization')
    _hybridization = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hybridization', [dirname(__file__)])
        except ImportError:
            import _hybridization
            return _hybridization
        try:
            _mod = imp.load_module('_hybridization', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _hybridization = swig_import_helper()
    del swig_import_helper
else:
    import _hybridization
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


import mfem._par.handle
import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.hypre
import mfem._par.sparsemat
import mfem._par.matrix
import mfem._par.densemat
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.intrules
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
class Hybridization(_object):
    """Proxy of C++ mfem::Hybridization class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hybridization, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Hybridization, name)
    __repr__ = _swig_repr

    def __init__(self, fespace, c_fespace):
        """__init__(mfem::Hybridization self, FiniteElementSpace fespace, FiniteElementSpace c_fespace) -> Hybridization"""
        this = _hybridization.new_Hybridization(fespace, c_fespace)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hybridization.delete_Hybridization
    __del__ = lambda self: None

    def SetConstraintIntegrator(self, c_integ):
        """SetConstraintIntegrator(Hybridization self, BilinearFormIntegrator c_integ)"""
        return _hybridization.Hybridization_SetConstraintIntegrator(self, c_integ)


    def Init(self, ess_tdof_list):
        """Init(Hybridization self, intArray ess_tdof_list)"""
        return _hybridization.Hybridization_Init(self, ess_tdof_list)


    def AssembleMatrix(self, el, A):
        """AssembleMatrix(Hybridization self, int el, DenseMatrix A)"""
        return _hybridization.Hybridization_AssembleMatrix(self, el, A)


    def AssembleBdrMatrix(self, bdr_el, A):
        """AssembleBdrMatrix(Hybridization self, int bdr_el, DenseMatrix A)"""
        return _hybridization.Hybridization_AssembleBdrMatrix(self, bdr_el, A)


    def Finalize(self):
        """Finalize(Hybridization self)"""
        return _hybridization.Hybridization_Finalize(self)


    def GetMatrix(self):
        """GetMatrix(Hybridization self) -> SparseMatrix"""
        return _hybridization.Hybridization_GetMatrix(self)


    def GetParallelMatrix(self, *args):
        """
        GetParallelMatrix(Hybridization self) -> HypreParMatrix
        GetParallelMatrix(Hybridization self, OperatorHandle H_h)
        """
        return _hybridization.Hybridization_GetParallelMatrix(self, *args)


    def SetOperatorType(self, tid):
        """SetOperatorType(Hybridization self, mfem::Operator::Type tid)"""
        return _hybridization.Hybridization_SetOperatorType(self, tid)


    def ReduceRHS(self, b, b_r):
        """ReduceRHS(Hybridization self, Vector b, Vector b_r)"""
        return _hybridization.Hybridization_ReduceRHS(self, b, b_r)


    def ComputeSolution(self, b, sol_r, sol):
        """ComputeSolution(Hybridization self, Vector b, Vector sol_r, Vector sol)"""
        return _hybridization.Hybridization_ComputeSolution(self, b, sol_r, sol)


    def Reset(self):
        """Reset(Hybridization self)"""
        return _hybridization.Hybridization_Reset(self)

Hybridization_swigregister = _hybridization.Hybridization_swigregister
Hybridization_swigregister(Hybridization)

# This file is compatible with both classic and new-style classes.


