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
        mname = '.'.join((pkg, '_solvers')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_solvers')
    _solvers = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_solvers', [dirname(__file__)])
        except ImportError:
            import _solvers
            return _solvers
        try:
            _mod = imp.load_module('_solvers', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _solvers = swig_import_helper()
    del swig_import_helper
else:
    import _solvers
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


MFEM_VERSION = _solvers.MFEM_VERSION
MFEM_VERSION_STRING = _solvers.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _solvers.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _solvers.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _solvers.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _solvers.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _solvers.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _solvers.MFEM_VERSION_PATCH
MFEM_TIMER_TYPE = _solvers.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _solvers.MFEM_HYPRE_VERSION
import vector
import array
import ostream_typemap
import operators
import matrix
import sparsemat
import densemat
class IterativeSolver(operators.Solver):
    __swig_setmethods__ = {}
    for _s in [operators.Solver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IterativeSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [operators.Solver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IterativeSolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetRelTol(self, rtol):
        return _solvers.IterativeSolver_SetRelTol(self, rtol)

    def SetAbsTol(self, atol):
        return _solvers.IterativeSolver_SetAbsTol(self, atol)

    def SetMaxIter(self, max_it):
        return _solvers.IterativeSolver_SetMaxIter(self, max_it)

    def SetPrintLevel(self, print_lvl):
        return _solvers.IterativeSolver_SetPrintLevel(self, print_lvl)

    def GetNumIterations(self):
        return _solvers.IterativeSolver_GetNumIterations(self)

    def GetConverged(self):
        return _solvers.IterativeSolver_GetConverged(self)

    def GetFinalNorm(self):
        return _solvers.IterativeSolver_GetFinalNorm(self)

    def SetPreconditioner(self, pr):
        return _solvers.IterativeSolver_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        return _solvers.IterativeSolver_SetOperator(self, op)
    __swig_destroy__ = _solvers.delete_IterativeSolver
    __del__ = lambda self: None
IterativeSolver_swigregister = _solvers.IterativeSolver_swigregister
IterativeSolver_swigregister(IterativeSolver)

class SLISolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SLISolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SLISolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_SLISolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        return _solvers.SLISolver_SetOperator(self, op)

    def Mult(self, b, x):
        return _solvers.SLISolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_SLISolver
    __del__ = lambda self: None
SLISolver_swigregister = _solvers.SLISolver_swigregister
SLISolver_swigregister(SLISolver)


def SLI(*args):
    return _solvers.SLI(*args)
SLI = _solvers.SLI
class CGSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CGSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CGSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_CGSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        return _solvers.CGSolver_SetOperator(self, op)

    def Mult(self, b, x):
        return _solvers.CGSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_CGSolver
    __del__ = lambda self: None
CGSolver_swigregister = _solvers.CGSolver_swigregister
CGSolver_swigregister(CGSolver)


def CG(A, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    return _solvers.CG(A, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)
CG = _solvers.CG

def PCG(A, B, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    return _solvers.PCG(A, B, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)
PCG = _solvers.PCG
class GMRESSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GMRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GMRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_GMRESSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetKDim(self, dim):
        return _solvers.GMRESSolver_SetKDim(self, dim)

    def Mult(self, b, x):
        return _solvers.GMRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_GMRESSolver
    __del__ = lambda self: None
GMRESSolver_swigregister = _solvers.GMRESSolver_swigregister
GMRESSolver_swigregister(GMRESSolver)

class FGMRESSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FGMRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FGMRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_FGMRESSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetKDim(self, dim):
        return _solvers.FGMRESSolver_SetKDim(self, dim)

    def Mult(self, b, x):
        return _solvers.FGMRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_FGMRESSolver
    __del__ = lambda self: None
FGMRESSolver_swigregister = _solvers.FGMRESSolver_swigregister
FGMRESSolver_swigregister(FGMRESSolver)


def GMRES(*args):
    return _solvers.GMRES(*args)
GMRES = _solvers.GMRES
class BiCGSTABSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BiCGSTABSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BiCGSTABSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_BiCGSTABSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        return _solvers.BiCGSTABSolver_SetOperator(self, op)

    def Mult(self, b, x):
        return _solvers.BiCGSTABSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_BiCGSTABSolver
    __del__ = lambda self: None
BiCGSTABSolver_swigregister = _solvers.BiCGSTABSolver_swigregister
BiCGSTABSolver_swigregister(BiCGSTABSolver)


def BiCGSTAB(*args):
    return _solvers.BiCGSTAB(*args)
BiCGSTAB = _solvers.BiCGSTAB
class MINRESSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MINRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MINRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_MINRESSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetPreconditioner(self, pr):
        return _solvers.MINRESSolver_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        return _solvers.MINRESSolver_SetOperator(self, op)

    def Mult(self, b, x):
        return _solvers.MINRESSolver_Mult(self, b, x)
    __swig_destroy__ = _solvers.delete_MINRESSolver
    __del__ = lambda self: None
MINRESSolver_swigregister = _solvers.MINRESSolver_swigregister
MINRESSolver_swigregister(MINRESSolver)


def MINRES(*args):
    return _solvers.MINRES(*args)
MINRES = _solvers.MINRES
class NewtonSolver(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NewtonSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NewtonSolver, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_NewtonSolver(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        return _solvers.NewtonSolver_SetOperator(self, op)

    def SetSolver(self, solver):
        return _solvers.NewtonSolver_SetSolver(self, solver)

    def Mult(self, b, x):
        return _solvers.NewtonSolver_Mult(self, b, x)

    def ComputeScalingFactor(self, x, b):
        return _solvers.NewtonSolver_ComputeScalingFactor(self, x, b)
    __swig_destroy__ = _solvers.delete_NewtonSolver
    __del__ = lambda self: None
NewtonSolver_swigregister = _solvers.NewtonSolver_swigregister
NewtonSolver_swigregister(NewtonSolver)


def aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit):
    return _solvers.aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit)
aGMRES = _solvers.aGMRES
class SLBQPOptimizer(IterativeSolver):
    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SLBQPOptimizer, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SLBQPOptimizer, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _solvers.new_SLBQPOptimizer(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetBounds(self, _lo, _hi):
        return _solvers.SLBQPOptimizer_SetBounds(self, _lo, _hi)

    def SetLinearConstraint(self, _w, _a):
        return _solvers.SLBQPOptimizer_SetLinearConstraint(self, _w, _a)

    def Mult(self, xt, x):
        return _solvers.SLBQPOptimizer_Mult(self, xt, x)

    def SetPreconditioner(self, pr):
        return _solvers.SLBQPOptimizer_SetPreconditioner(self, pr)

    def SetOperator(self, op):
        return _solvers.SLBQPOptimizer_SetOperator(self, op)
    __swig_destroy__ = _solvers.delete_SLBQPOptimizer
    __del__ = lambda self: None
SLBQPOptimizer_swigregister = _solvers.SLBQPOptimizer_swigregister
SLBQPOptimizer_swigregister(SLBQPOptimizer)

# This file is compatible with both classic and new-style classes.


