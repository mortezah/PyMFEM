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
        mname = '.'.join((pkg, '_ode')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ode')
    _ode = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ode', [dirname(__file__)])
        except ImportError:
            import _ode
            return _ode
        try:
            _mod = imp.load_module('_ode', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ode = swig_import_helper()
    del swig_import_helper
else:
    import _ode
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
class ODESolver(_object):
    """Proxy of C++ mfem::ODESolver class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ODESolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ODESolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Init(self, f):
        """Init(ODESolver self, TimeDependentOperator f)"""
        return _ode.ODESolver_Init(self, f)


    def Step(self, x, t, dt):
        """Step(ODESolver self, Vector x, double & t, double & dt)"""
        return _ode.ODESolver_Step(self, x, t, dt)


    def Run(self, x, t, dt, tf):
        """Run(ODESolver self, Vector x, double & t, double & dt, double tf)"""
        return _ode.ODESolver_Run(self, x, t, dt, tf)

    __swig_destroy__ = _ode.delete_ODESolver
    __del__ = lambda self: None
ODESolver_swigregister = _ode.ODESolver_swigregister
ODESolver_swigregister(ODESolver)

class ForwardEulerSolver(ODESolver):
    """Proxy of C++ mfem::ForwardEulerSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ForwardEulerSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ForwardEulerSolver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(ForwardEulerSolver self, TimeDependentOperator _f)"""
        return _ode.ForwardEulerSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(ForwardEulerSolver self, Vector x, double & t, double & dt)"""
        return _ode.ForwardEulerSolver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::ForwardEulerSolver self) -> ForwardEulerSolver"""
        this = _ode.new_ForwardEulerSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_ForwardEulerSolver
    __del__ = lambda self: None
ForwardEulerSolver_swigregister = _ode.ForwardEulerSolver_swigregister
ForwardEulerSolver_swigregister(ForwardEulerSolver)

class RK2Solver(ODESolver):
    """Proxy of C++ mfem::RK2Solver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RK2Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RK2Solver, name)
    __repr__ = _swig_repr

    def __init__(self, _a=2):
        """
        __init__(mfem::RK2Solver self, double const _a=2) -> RK2Solver
        __init__(mfem::RK2Solver self) -> RK2Solver
        """
        this = _ode.new_RK2Solver(_a)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Init(self, _f):
        """Init(RK2Solver self, TimeDependentOperator _f)"""
        return _ode.RK2Solver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(RK2Solver self, Vector x, double & t, double & dt)"""
        return _ode.RK2Solver_Step(self, x, t, dt)

    __swig_destroy__ = _ode.delete_RK2Solver
    __del__ = lambda self: None
RK2Solver_swigregister = _ode.RK2Solver_swigregister
RK2Solver_swigregister(RK2Solver)

class RK3SSPSolver(ODESolver):
    """Proxy of C++ mfem::RK3SSPSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RK3SSPSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RK3SSPSolver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(RK3SSPSolver self, TimeDependentOperator _f)"""
        return _ode.RK3SSPSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(RK3SSPSolver self, Vector x, double & t, double & dt)"""
        return _ode.RK3SSPSolver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::RK3SSPSolver self) -> RK3SSPSolver"""
        this = _ode.new_RK3SSPSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_RK3SSPSolver
    __del__ = lambda self: None
RK3SSPSolver_swigregister = _ode.RK3SSPSolver_swigregister
RK3SSPSolver_swigregister(RK3SSPSolver)

class RK4Solver(ODESolver):
    """Proxy of C++ mfem::RK4Solver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RK4Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RK4Solver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(RK4Solver self, TimeDependentOperator _f)"""
        return _ode.RK4Solver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(RK4Solver self, Vector x, double & t, double & dt)"""
        return _ode.RK4Solver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::RK4Solver self) -> RK4Solver"""
        this = _ode.new_RK4Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_RK4Solver
    __del__ = lambda self: None
RK4Solver_swigregister = _ode.RK4Solver_swigregister
RK4Solver_swigregister(RK4Solver)

class ExplicitRKSolver(ODESolver):
    """Proxy of C++ mfem::ExplicitRKSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExplicitRKSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ExplicitRKSolver, name)
    __repr__ = _swig_repr

    def __init__(self, _s, _a, _b, _c):
        """__init__(mfem::ExplicitRKSolver self, int _s, double const * _a, double const * _b, double const * _c) -> ExplicitRKSolver"""
        this = _ode.new_ExplicitRKSolver(_s, _a, _b, _c)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Init(self, _f):
        """Init(ExplicitRKSolver self, TimeDependentOperator _f)"""
        return _ode.ExplicitRKSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(ExplicitRKSolver self, Vector x, double & t, double & dt)"""
        return _ode.ExplicitRKSolver_Step(self, x, t, dt)

    __swig_destroy__ = _ode.delete_ExplicitRKSolver
    __del__ = lambda self: None
ExplicitRKSolver_swigregister = _ode.ExplicitRKSolver_swigregister
ExplicitRKSolver_swigregister(ExplicitRKSolver)

class RK6Solver(ExplicitRKSolver):
    """Proxy of C++ mfem::RK6Solver class."""

    __swig_setmethods__ = {}
    for _s in [ExplicitRKSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RK6Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ExplicitRKSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RK6Solver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::RK6Solver self) -> RK6Solver"""
        this = _ode.new_RK6Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_RK6Solver
    __del__ = lambda self: None
RK6Solver_swigregister = _ode.RK6Solver_swigregister
RK6Solver_swigregister(RK6Solver)

class RK8Solver(ExplicitRKSolver):
    """Proxy of C++ mfem::RK8Solver class."""

    __swig_setmethods__ = {}
    for _s in [ExplicitRKSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RK8Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ExplicitRKSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RK8Solver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::RK8Solver self) -> RK8Solver"""
        this = _ode.new_RK8Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_RK8Solver
    __del__ = lambda self: None
RK8Solver_swigregister = _ode.RK8Solver_swigregister
RK8Solver_swigregister(RK8Solver)

class BackwardEulerSolver(ODESolver):
    """Proxy of C++ mfem::BackwardEulerSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BackwardEulerSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BackwardEulerSolver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(BackwardEulerSolver self, TimeDependentOperator _f)"""
        return _ode.BackwardEulerSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(BackwardEulerSolver self, Vector x, double & t, double & dt)"""
        return _ode.BackwardEulerSolver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::BackwardEulerSolver self) -> BackwardEulerSolver"""
        this = _ode.new_BackwardEulerSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_BackwardEulerSolver
    __del__ = lambda self: None
BackwardEulerSolver_swigregister = _ode.BackwardEulerSolver_swigregister
BackwardEulerSolver_swigregister(BackwardEulerSolver)

class ImplicitMidpointSolver(ODESolver):
    """Proxy of C++ mfem::ImplicitMidpointSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImplicitMidpointSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ImplicitMidpointSolver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(ImplicitMidpointSolver self, TimeDependentOperator _f)"""
        return _ode.ImplicitMidpointSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(ImplicitMidpointSolver self, Vector x, double & t, double & dt)"""
        return _ode.ImplicitMidpointSolver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::ImplicitMidpointSolver self) -> ImplicitMidpointSolver"""
        this = _ode.new_ImplicitMidpointSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_ImplicitMidpointSolver
    __del__ = lambda self: None
ImplicitMidpointSolver_swigregister = _ode.ImplicitMidpointSolver_swigregister
ImplicitMidpointSolver_swigregister(ImplicitMidpointSolver)

class SDIRK23Solver(ODESolver):
    """Proxy of C++ mfem::SDIRK23Solver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SDIRK23Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SDIRK23Solver, name)
    __repr__ = _swig_repr

    def __init__(self, gamma_opt=1):
        """
        __init__(mfem::SDIRK23Solver self, int gamma_opt=1) -> SDIRK23Solver
        __init__(mfem::SDIRK23Solver self) -> SDIRK23Solver
        """
        this = _ode.new_SDIRK23Solver(gamma_opt)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Init(self, _f):
        """Init(SDIRK23Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK23Solver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(SDIRK23Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK23Solver_Step(self, x, t, dt)

    __swig_destroy__ = _ode.delete_SDIRK23Solver
    __del__ = lambda self: None
SDIRK23Solver_swigregister = _ode.SDIRK23Solver_swigregister
SDIRK23Solver_swigregister(SDIRK23Solver)

class SDIRK34Solver(ODESolver):
    """Proxy of C++ mfem::SDIRK34Solver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SDIRK34Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SDIRK34Solver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(SDIRK34Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK34Solver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(SDIRK34Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK34Solver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::SDIRK34Solver self) -> SDIRK34Solver"""
        this = _ode.new_SDIRK34Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_SDIRK34Solver
    __del__ = lambda self: None
SDIRK34Solver_swigregister = _ode.SDIRK34Solver_swigregister
SDIRK34Solver_swigregister(SDIRK34Solver)

class SDIRK33Solver(ODESolver):
    """Proxy of C++ mfem::SDIRK33Solver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SDIRK33Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SDIRK33Solver, name)
    __repr__ = _swig_repr

    def Init(self, _f):
        """Init(SDIRK33Solver self, TimeDependentOperator _f)"""
        return _ode.SDIRK33Solver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(SDIRK33Solver self, Vector x, double & t, double & dt)"""
        return _ode.SDIRK33Solver_Step(self, x, t, dt)


    def __init__(self):
        """__init__(mfem::SDIRK33Solver self) -> SDIRK33Solver"""
        this = _ode.new_SDIRK33Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ode.delete_SDIRK33Solver
    __del__ = lambda self: None
SDIRK33Solver_swigregister = _ode.SDIRK33Solver_swigregister
SDIRK33Solver_swigregister(SDIRK33Solver)

class GeneralizedAlphaSolver(ODESolver):
    """Proxy of C++ mfem::GeneralizedAlphaSolver class."""

    __swig_setmethods__ = {}
    for _s in [ODESolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeneralizedAlphaSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [ODESolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GeneralizedAlphaSolver, name)
    __repr__ = _swig_repr

    def __init__(self, rho=1.0):
        """
        __init__(mfem::GeneralizedAlphaSolver self, double rho=1.0) -> GeneralizedAlphaSolver
        __init__(mfem::GeneralizedAlphaSolver self) -> GeneralizedAlphaSolver
        """
        this = _ode.new_GeneralizedAlphaSolver(rho)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Init(self, _f):
        """Init(GeneralizedAlphaSolver self, TimeDependentOperator _f)"""
        return _ode.GeneralizedAlphaSolver_Init(self, _f)


    def Step(self, x, t, dt):
        """Step(GeneralizedAlphaSolver self, Vector x, double & t, double & dt)"""
        return _ode.GeneralizedAlphaSolver_Step(self, x, t, dt)

    __swig_destroy__ = _ode.delete_GeneralizedAlphaSolver
    __del__ = lambda self: None
GeneralizedAlphaSolver_swigregister = _ode.GeneralizedAlphaSolver_swigregister
GeneralizedAlphaSolver_swigregister(GeneralizedAlphaSolver)

class SIASolver(_object):
    """Proxy of C++ mfem::SIASolver class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SIASolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SIASolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Init(self, P, F):
        """Init(SIASolver self, Operator P, TimeDependentOperator F)"""
        return _ode.SIASolver_Init(self, P, F)


    def Step(self, q, p, t, dt):
        """Step(SIASolver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIASolver_Step(self, q, p, t, dt)


    def Run(self, q, p, t, dt, tf):
        """Run(SIASolver self, Vector q, Vector p, double & t, double & dt, double tf)"""
        return _ode.SIASolver_Run(self, q, p, t, dt, tf)

    __swig_destroy__ = _ode.delete_SIASolver
    __del__ = lambda self: None
SIASolver_swigregister = _ode.SIASolver_swigregister
SIASolver_swigregister(SIASolver)

class SIA1Solver(SIASolver):
    """Proxy of C++ mfem::SIA1Solver class."""

    __swig_setmethods__ = {}
    for _s in [SIASolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SIA1Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [SIASolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SIA1Solver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::SIA1Solver self) -> SIA1Solver"""
        this = _ode.new_SIA1Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Step(self, q, p, t, dt):
        """Step(SIA1Solver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIA1Solver_Step(self, q, p, t, dt)

    __swig_destroy__ = _ode.delete_SIA1Solver
    __del__ = lambda self: None
SIA1Solver_swigregister = _ode.SIA1Solver_swigregister
SIA1Solver_swigregister(SIA1Solver)

class SIA2Solver(SIASolver):
    """Proxy of C++ mfem::SIA2Solver class."""

    __swig_setmethods__ = {}
    for _s in [SIASolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SIA2Solver, name, value)
    __swig_getmethods__ = {}
    for _s in [SIASolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SIA2Solver, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(mfem::SIA2Solver self) -> SIA2Solver"""
        this = _ode.new_SIA2Solver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Step(self, q, p, t, dt):
        """Step(SIA2Solver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIA2Solver_Step(self, q, p, t, dt)

    __swig_destroy__ = _ode.delete_SIA2Solver
    __del__ = lambda self: None
SIA2Solver_swigregister = _ode.SIA2Solver_swigregister
SIA2Solver_swigregister(SIA2Solver)

class SIAVSolver(SIASolver):
    """Proxy of C++ mfem::SIAVSolver class."""

    __swig_setmethods__ = {}
    for _s in [SIASolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SIAVSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [SIASolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SIAVSolver, name)
    __repr__ = _swig_repr

    def __init__(self, order):
        """__init__(mfem::SIAVSolver self, int order) -> SIAVSolver"""
        this = _ode.new_SIAVSolver(order)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Step(self, q, p, t, dt):
        """Step(SIAVSolver self, Vector q, Vector p, double & t, double & dt)"""
        return _ode.SIAVSolver_Step(self, q, p, t, dt)

    __swig_destroy__ = _ode.delete_SIAVSolver
    __del__ = lambda self: None
SIAVSolver_swigregister = _ode.SIAVSolver_swigregister
SIAVSolver_swigregister(SIAVSolver)

# This file is compatible with both classic and new-style classes.


