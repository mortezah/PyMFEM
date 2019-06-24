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


import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.sparsemat
import mfem._ser.densemat
class IterativeSolver(mfem._ser.operators.Solver):
    """Proxy of C++ mfem::IterativeSolver class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.operators.Solver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IterativeSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.operators.Solver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IterativeSolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetRelTol(self, rtol):
        """SetRelTol(IterativeSolver self, double rtol)"""
        return _solvers.IterativeSolver_SetRelTol(self, rtol)


    def SetAbsTol(self, atol):
        """SetAbsTol(IterativeSolver self, double atol)"""
        return _solvers.IterativeSolver_SetAbsTol(self, atol)


    def SetMaxIter(self, max_it):
        """SetMaxIter(IterativeSolver self, int max_it)"""
        return _solvers.IterativeSolver_SetMaxIter(self, max_it)


    def SetPrintLevel(self, print_lvl):
        """SetPrintLevel(IterativeSolver self, int print_lvl)"""
        return _solvers.IterativeSolver_SetPrintLevel(self, print_lvl)


    def GetNumIterations(self):
        """GetNumIterations(IterativeSolver self) -> int"""
        return _solvers.IterativeSolver_GetNumIterations(self)


    def GetConverged(self):
        """GetConverged(IterativeSolver self) -> int"""
        return _solvers.IterativeSolver_GetConverged(self)


    def GetFinalNorm(self):
        """GetFinalNorm(IterativeSolver self) -> double"""
        return _solvers.IterativeSolver_GetFinalNorm(self)


    def SetPreconditioner(self, pr):
        """SetPreconditioner(IterativeSolver self, Solver pr)"""
        return _solvers.IterativeSolver_SetPreconditioner(self, pr)


    def SetOperator(self, op):
        """SetOperator(IterativeSolver self, Operator op)"""
        return _solvers.IterativeSolver_SetOperator(self, op)

    __swig_destroy__ = _solvers.delete_IterativeSolver
    __del__ = lambda self: None
IterativeSolver_swigregister = _solvers.IterativeSolver_swigregister
IterativeSolver_swigregister(IterativeSolver)

class SLISolver(IterativeSolver):
    """Proxy of C++ mfem::SLISolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SLISolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SLISolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::SLISolver self) -> SLISolver"""
        this = _solvers.new_SLISolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        """SetOperator(SLISolver self, Operator op)"""
        return _solvers.SLISolver_SetOperator(self, op)


    def Mult(self, b, x):
        """Mult(SLISolver self, Vector b, Vector x)"""
        return _solvers.SLISolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_SLISolver
    __del__ = lambda self: None
SLISolver_swigregister = _solvers.SLISolver_swigregister
SLISolver_swigregister(SLISolver)


def SLI(*args):
    """
    SLI(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    SLI(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12)
    SLI(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    SLI(Operator A, Vector b, Vector x, int print_iter=0)
    SLI(Operator A, Vector b, Vector x)
    SLI(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    SLI(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12)
    SLI(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    SLI(Operator A, Solver B, Vector b, Vector x, int print_iter=0)
    SLI(Operator A, Solver B, Vector b, Vector x)
    """
    return _solvers.SLI(*args)
class CGSolver(IterativeSolver):
    """Proxy of C++ mfem::CGSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CGSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CGSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::CGSolver self) -> CGSolver"""
        this = _solvers.new_CGSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        """SetOperator(CGSolver self, Operator op)"""
        return _solvers.CGSolver_SetOperator(self, op)


    def Mult(self, b, x):
        """Mult(CGSolver self, Vector b, Vector x)"""
        return _solvers.CGSolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_CGSolver
    __del__ = lambda self: None
CGSolver_swigregister = _solvers.CGSolver_swigregister
CGSolver_swigregister(CGSolver)


def CG(A, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    """
    CG(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    CG(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12)
    CG(Operator A, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    CG(Operator A, Vector b, Vector x, int print_iter=0)
    CG(Operator A, Vector b, Vector x)
    """
    return _solvers.CG(A, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)

def PCG(A, B, b, x, print_iter=0, max_num_iter=1000, RTOLERANCE=1e-12, ATOLERANCE=1e-24):
    """
    PCG(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12, double ATOLERANCE=1e-24)
    PCG(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double RTOLERANCE=1e-12)
    PCG(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    PCG(Operator A, Solver B, Vector b, Vector x, int print_iter=0)
    PCG(Operator A, Solver B, Vector b, Vector x)
    """
    return _solvers.PCG(A, B, b, x, print_iter, max_num_iter, RTOLERANCE, ATOLERANCE)
class GMRESSolver(IterativeSolver):
    """Proxy of C++ mfem::GMRESSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GMRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GMRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::GMRESSolver self) -> GMRESSolver"""
        this = _solvers.new_GMRESSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetKDim(self, dim):
        """SetKDim(GMRESSolver self, int dim)"""
        return _solvers.GMRESSolver_SetKDim(self, dim)


    def Mult(self, b, x):
        """Mult(GMRESSolver self, Vector b, Vector x)"""
        return _solvers.GMRESSolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_GMRESSolver
    __del__ = lambda self: None
GMRESSolver_swigregister = _solvers.GMRESSolver_swigregister
GMRESSolver_swigregister(GMRESSolver)

class FGMRESSolver(IterativeSolver):
    """Proxy of C++ mfem::FGMRESSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FGMRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FGMRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::FGMRESSolver self) -> FGMRESSolver"""
        this = _solvers.new_FGMRESSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetKDim(self, dim):
        """SetKDim(FGMRESSolver self, int dim)"""
        return _solvers.FGMRESSolver_SetKDim(self, dim)


    def Mult(self, b, x):
        """Mult(FGMRESSolver self, Vector b, Vector x)"""
        return _solvers.FGMRESSolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_FGMRESSolver
    __del__ = lambda self: None
FGMRESSolver_swigregister = _solvers.FGMRESSolver_swigregister
FGMRESSolver_swigregister(FGMRESSolver)


def GMRES(*args):
    """
    GMRES(Operator A, Vector x, Vector b, Solver M, int & max_iter, int m, double & tol, double atol, int printit) -> int
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, int m=50, double rtol=1e-12, double atol=1e-24)
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, int m=50, double rtol=1e-12)
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, int m=50)
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    GMRES(Operator A, Solver B, Vector b, Vector x, int print_iter=0)
    GMRES(Operator A, Solver B, Vector b, Vector x)
    """
    return _solvers.GMRES(*args)
class BiCGSTABSolver(IterativeSolver):
    """Proxy of C++ mfem::BiCGSTABSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BiCGSTABSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BiCGSTABSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::BiCGSTABSolver self) -> BiCGSTABSolver"""
        this = _solvers.new_BiCGSTABSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        """SetOperator(BiCGSTABSolver self, Operator op)"""
        return _solvers.BiCGSTABSolver_SetOperator(self, op)


    def Mult(self, b, x):
        """Mult(BiCGSTABSolver self, Vector b, Vector x)"""
        return _solvers.BiCGSTABSolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_BiCGSTABSolver
    __del__ = lambda self: None
BiCGSTABSolver_swigregister = _solvers.BiCGSTABSolver_swigregister
BiCGSTABSolver_swigregister(BiCGSTABSolver)


def BiCGSTAB(*args):
    """
    BiCGSTAB(Operator A, Vector x, Vector b, Solver M, int & max_iter, double & tol, double atol, int printit) -> int
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double rtol=1e-12, double atol=1e-24)
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000, double rtol=1e-12)
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x, int print_iter=0, int max_num_iter=1000)
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x, int print_iter=0)
    BiCGSTAB(Operator A, Solver B, Vector b, Vector x)
    """
    return _solvers.BiCGSTAB(*args)
class MINRESSolver(IterativeSolver):
    """Proxy of C++ mfem::MINRESSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MINRESSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MINRESSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::MINRESSolver self) -> MINRESSolver"""
        this = _solvers.new_MINRESSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetPreconditioner(self, pr):
        """SetPreconditioner(MINRESSolver self, Solver pr)"""
        return _solvers.MINRESSolver_SetPreconditioner(self, pr)


    def SetOperator(self, op):
        """SetOperator(MINRESSolver self, Operator op)"""
        return _solvers.MINRESSolver_SetOperator(self, op)


    def Mult(self, b, x):
        """Mult(MINRESSolver self, Vector b, Vector x)"""
        return _solvers.MINRESSolver_Mult(self, b, x)

    __swig_destroy__ = _solvers.delete_MINRESSolver
    __del__ = lambda self: None
MINRESSolver_swigregister = _solvers.MINRESSolver_swigregister
MINRESSolver_swigregister(MINRESSolver)


def MINRES(*args):
    """
    MINRES(Operator A, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12, double atol=1e-24)
    MINRES(Operator A, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12)
    MINRES(Operator A, Vector b, Vector x, int print_it=0, int max_it=1000)
    MINRES(Operator A, Vector b, Vector x, int print_it=0)
    MINRES(Operator A, Vector b, Vector x)
    MINRES(Operator A, Solver B, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12, double atol=1e-24)
    MINRES(Operator A, Solver B, Vector b, Vector x, int print_it=0, int max_it=1000, double rtol=1e-12)
    MINRES(Operator A, Solver B, Vector b, Vector x, int print_it=0, int max_it=1000)
    MINRES(Operator A, Solver B, Vector b, Vector x, int print_it=0)
    MINRES(Operator A, Solver B, Vector b, Vector x)
    """
    return _solvers.MINRES(*args)
class NewtonSolver(IterativeSolver):
    """Proxy of C++ mfem::NewtonSolver class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NewtonSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NewtonSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::NewtonSolver self) -> NewtonSolver"""
        this = _solvers.new_NewtonSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetOperator(self, op):
        """SetOperator(NewtonSolver self, Operator op)"""
        return _solvers.NewtonSolver_SetOperator(self, op)


    def SetSolver(self, solver):
        """SetSolver(NewtonSolver self, Solver solver)"""
        return _solvers.NewtonSolver_SetSolver(self, solver)


    def Mult(self, b, x):
        """Mult(NewtonSolver self, Vector b, Vector x)"""
        return _solvers.NewtonSolver_Mult(self, b, x)


    def ComputeScalingFactor(self, x, b):
        """ComputeScalingFactor(NewtonSolver self, Vector x, Vector b) -> double"""
        return _solvers.NewtonSolver_ComputeScalingFactor(self, x, b)

    __swig_destroy__ = _solvers.delete_NewtonSolver
    __del__ = lambda self: None
NewtonSolver_swigregister = _solvers.NewtonSolver_swigregister
NewtonSolver_swigregister(NewtonSolver)


def aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit):
    """aGMRES(Operator A, Vector x, Vector b, Operator M, int & max_iter, int m_max, int m_min, int m_step, double cf, double & tol, double & atol, int printit) -> int"""
    return _solvers.aGMRES(A, x, b, M, max_iter, m_max, m_min, m_step, cf, tol, atol, printit)
class SLBQPOptimizer(IterativeSolver):
    """Proxy of C++ mfem::SLBQPOptimizer class."""

    __swig_setmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SLBQPOptimizer, name, value)
    __swig_getmethods__ = {}
    for _s in [IterativeSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SLBQPOptimizer, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::SLBQPOptimizer self) -> SLBQPOptimizer"""
        this = _solvers.new_SLBQPOptimizer()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetBounds(self, _lo, _hi):
        """SetBounds(SLBQPOptimizer self, Vector _lo, Vector _hi)"""
        return _solvers.SLBQPOptimizer_SetBounds(self, _lo, _hi)


    def SetLinearConstraint(self, _w, _a):
        """SetLinearConstraint(SLBQPOptimizer self, Vector _w, double _a)"""
        return _solvers.SLBQPOptimizer_SetLinearConstraint(self, _w, _a)


    def Mult(self, xt, x):
        """Mult(SLBQPOptimizer self, Vector xt, Vector x)"""
        return _solvers.SLBQPOptimizer_Mult(self, xt, x)


    def SetPreconditioner(self, pr):
        """SetPreconditioner(SLBQPOptimizer self, Solver pr)"""
        return _solvers.SLBQPOptimizer_SetPreconditioner(self, pr)


    def SetOperator(self, op):
        """SetOperator(SLBQPOptimizer self, Operator op)"""
        return _solvers.SLBQPOptimizer_SetOperator(self, op)

    __swig_destroy__ = _solvers.delete_SLBQPOptimizer
    __del__ = lambda self: None
SLBQPOptimizer_swigregister = _solvers.SLBQPOptimizer_swigregister
SLBQPOptimizer_swigregister(SLBQPOptimizer)

# This file is compatible with both classic and new-style classes.


