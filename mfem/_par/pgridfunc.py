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
        mname = '.'.join((pkg, '_pgridfunc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pgridfunc')
    _pgridfunc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pgridfunc', [dirname(__file__)])
        except ImportError:
            import _pgridfunc
            return _pgridfunc
        try:
            _mod = imp.load_module('_pgridfunc', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pgridfunc = swig_import_helper()
    del swig_import_helper
else:
    import _pgridfunc
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


MFEM_VERSION = _pgridfunc.MFEM_VERSION
MFEM_VERSION_STRING = _pgridfunc.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pgridfunc.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pgridfunc.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pgridfunc.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pgridfunc.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pgridfunc.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pgridfunc.MFEM_VERSION_PATCH
MFEM_TIMER_TYPE = _pgridfunc.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _pgridfunc.MFEM_HYPRE_VERSION
import mfem._par.pfespace
import mfem._par.operators
import mfem._par.vector
import mfem._par.array
import mfem._par.ostream_typemap
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.geom
import mfem._par.table
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets

def GlobalLpNorm(p, loc_norm, comm):
    """GlobalLpNorm(double const p, double loc_norm, MPI_Comm comm) -> double"""
    return _pgridfunc.GlobalLpNorm(p, loc_norm, comm)
class ParGridFunction(mfem._par.gridfunc.GridFunction):
    """Proxy of C++ mfem::ParGridFunction class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.gridfunc.GridFunction]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParGridFunction, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.gridfunc.GridFunction]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParGridFunction, name)
    __repr__ = _swig_repr

    def ParFESpace(self):
        """ParFESpace(ParGridFunction self) -> ParFiniteElementSpace"""
        return _pgridfunc.ParGridFunction_ParFESpace(self)


    def Update(self):
        """Update(ParGridFunction self)"""
        return _pgridfunc.ParGridFunction_Update(self)


    def SetSpace(self, *args):
        """
        SetSpace(ParGridFunction self, FiniteElementSpace f)
        SetSpace(ParGridFunction self, ParFiniteElementSpace f)
        """
        return _pgridfunc.ParGridFunction_SetSpace(self, *args)


    def MakeRef(self, *args):
        """
        MakeRef(ParGridFunction self, FiniteElementSpace f, double * v)
        MakeRef(ParGridFunction self, ParFiniteElementSpace f, double * v)
        MakeRef(ParGridFunction self, FiniteElementSpace f, Vector v, int v_offset)
        MakeRef(ParGridFunction self, ParFiniteElementSpace f, Vector v, int v_offset)
        """
        return _pgridfunc.ParGridFunction_MakeRef(self, *args)


    def Distribute(self, *args):
        """
        Distribute(ParGridFunction self, Vector tv)
        Distribute(ParGridFunction self, Vector tv)
        """
        return _pgridfunc.ParGridFunction_Distribute(self, *args)


    def AddDistribute(self, *args):
        """
        AddDistribute(ParGridFunction self, double a, Vector tv)
        AddDistribute(ParGridFunction self, double a, Vector tv)
        """
        return _pgridfunc.ParGridFunction_AddDistribute(self, *args)


    def SetFromTrueDofs(self, tv):
        """SetFromTrueDofs(ParGridFunction self, Vector tv)"""
        return _pgridfunc.ParGridFunction_SetFromTrueDofs(self, tv)


    def Assign(self, *args):
        """
        Assign(ParGridFunction self, double value) -> ParGridFunction
        Assign(ParGridFunction self, Vector v) -> ParGridFunction
        Assign(ParGridFunction self, HypreParVector tv) -> ParGridFunction
        """
        return _pgridfunc.ParGridFunction_Assign(self, *args)


    def GetTrueDofs(self, *args):
        """
        GetTrueDofs(ParGridFunction self, Vector tv)
        GetTrueDofs(ParGridFunction self) -> HypreParVector
        """
        return _pgridfunc.ParGridFunction_GetTrueDofs(self, *args)


    def ParallelAverage(self, *args):
        """
        ParallelAverage(ParGridFunction self, Vector tv)
        ParallelAverage(ParGridFunction self, HypreParVector tv)
        ParallelAverage(ParGridFunction self) -> HypreParVector
        """
        return _pgridfunc.ParGridFunction_ParallelAverage(self, *args)


    def ParallelProject(self, *args):
        """
        ParallelProject(ParGridFunction self, Vector tv)
        ParallelProject(ParGridFunction self, HypreParVector tv)
        ParallelProject(ParGridFunction self) -> HypreParVector
        """
        return _pgridfunc.ParGridFunction_ParallelProject(self, *args)


    def ParallelAssemble(self, *args):
        """
        ParallelAssemble(ParGridFunction self, Vector tv)
        ParallelAssemble(ParGridFunction self, HypreParVector tv)
        ParallelAssemble(ParGridFunction self) -> HypreParVector
        """
        return _pgridfunc.ParGridFunction_ParallelAssemble(self, *args)


    def ExchangeFaceNbrData(self):
        """ExchangeFaceNbrData(ParGridFunction self)"""
        return _pgridfunc.ParGridFunction_ExchangeFaceNbrData(self)


    def FaceNbrData(self, *args):
        """
        FaceNbrData(ParGridFunction self) -> Vector
        FaceNbrData(ParGridFunction self) -> Vector
        """
        return _pgridfunc.ParGridFunction_FaceNbrData(self, *args)


    def GetValue(self, *args):
        """
        GetValue(ParGridFunction self, int i, IntegrationPoint ip, int vdim=1) -> double
        GetValue(ParGridFunction self, int i, IntegrationPoint ip) -> double
        GetValue(ParGridFunction self, ElementTransformation T) -> double
        """
        return _pgridfunc.ParGridFunction_GetValue(self, *args)


    def ProjectCoefficient(self, *args):
        """
        ProjectCoefficient(ParGridFunction self, Coefficient coeff)
        ProjectCoefficient(ParGridFunction self, Coefficient coeff, intArray dofs, int vd=0)
        ProjectCoefficient(ParGridFunction self, Coefficient coeff, intArray dofs)
        ProjectCoefficient(ParGridFunction self, VectorCoefficient vcoeff)
        ProjectCoefficient(ParGridFunction self, VectorCoefficient vcoeff, intArray dofs)
        ProjectCoefficient(ParGridFunction self, mfem::Coefficient *[] coeff)
        ProjectCoefficient(ParGridFunction self, Coefficient coeff)
        """
        return _pgridfunc.ParGridFunction_ProjectCoefficient(self, *args)


    def ProjectDiscCoefficient(self, *args):
        """
        ProjectDiscCoefficient(ParGridFunction self, VectorCoefficient coeff, intArray dof_attr)
        ProjectDiscCoefficient(ParGridFunction self, VectorCoefficient coeff)
        ProjectDiscCoefficient(ParGridFunction self, Coefficient coeff, mfem::GridFunction::AvgType type)
        ProjectDiscCoefficient(ParGridFunction self, VectorCoefficient coeff, mfem::GridFunction::AvgType type)
        ProjectDiscCoefficient(ParGridFunction self, VectorCoefficient coeff)
        ProjectDiscCoefficient(ParGridFunction self, Coefficient coeff, mfem::GridFunction::AvgType type)
        ProjectDiscCoefficient(ParGridFunction self, VectorCoefficient vcoeff, mfem::GridFunction::AvgType type)
        """
        return _pgridfunc.ParGridFunction_ProjectDiscCoefficient(self, *args)


    def ComputeL1Error(self, *args):
        """
        ComputeL1Error(ParGridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(ParGridFunction self, mfem::Coefficient *[] exsol) -> double
        ComputeL1Error(ParGridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(ParGridFunction self, Coefficient exsol) -> double
        ComputeL1Error(ParGridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(ParGridFunction self, VectorCoefficient exsol) -> double
        """
        return _pgridfunc.ParGridFunction_ComputeL1Error(self, *args)


    def ComputeL2Error(self, *args):
        """
        ComputeL2Error(ParGridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(ParGridFunction self, mfem::Coefficient *[] exsol) -> double
        ComputeL2Error(ParGridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(ParGridFunction self, Coefficient exsol) -> double
        ComputeL2Error(ParGridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0, intArray elems=None) -> double
        ComputeL2Error(ParGridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(ParGridFunction self, VectorCoefficient exsol) -> double
        """
        return _pgridfunc.ParGridFunction_ComputeL2Error(self, *args)


    def ComputeMaxError(self, *args):
        """
        ComputeMaxError(ParGridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(ParGridFunction self, mfem::Coefficient *[] exsol) -> double
        ComputeMaxError(ParGridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(ParGridFunction self, Coefficient exsol) -> double
        ComputeMaxError(ParGridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(ParGridFunction self, VectorCoefficient exsol) -> double
        """
        return _pgridfunc.ParGridFunction_ComputeMaxError(self, *args)


    def ComputeLpError(self, *args):
        """
        ComputeLpError(ParGridFunction self, double const p, Coefficient exsol, Coefficient weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeLpError(ParGridFunction self, double const p, Coefficient exsol, Coefficient weight=None) -> double
        ComputeLpError(ParGridFunction self, double const p, Coefficient exsol) -> double
        ComputeLpError(ParGridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None, VectorCoefficient v_weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeLpError(ParGridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None, VectorCoefficient v_weight=None) -> double
        ComputeLpError(ParGridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None) -> double
        ComputeLpError(ParGridFunction self, double const p, VectorCoefficient exsol) -> double
        """
        return _pgridfunc.ParGridFunction_ComputeLpError(self, *args)


    def ComputeFlux(self, blfi, flux, wcoef=1, subdomain=-1):
        """
        ComputeFlux(ParGridFunction self, BilinearFormIntegrator blfi, GridFunction flux, int wcoef=1, int subdomain=-1)
        ComputeFlux(ParGridFunction self, BilinearFormIntegrator blfi, GridFunction flux, int wcoef=1)
        ComputeFlux(ParGridFunction self, BilinearFormIntegrator blfi, GridFunction flux)
        """
        return _pgridfunc.ParGridFunction_ComputeFlux(self, blfi, flux, wcoef, subdomain)


    def Save(self, out):
        """Save(ParGridFunction self, std::ostream & out)"""
        return _pgridfunc.ParGridFunction_Save(self, out)


    def SaveAsOne(self, *args):
        """
        SaveAsOne(ParGridFunction self, std::ostream & out)
        SaveAsOne(ParGridFunction self)
        """
        return _pgridfunc.ParGridFunction_SaveAsOne(self, *args)

    __swig_destroy__ = _pgridfunc.delete_ParGridFunction
    __del__ = lambda self: None

    def __init__(self, *args):
        """
        __init__(mfem::ParGridFunction self) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParFiniteElementSpace pf) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParFiniteElementSpace pf, double * data) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParFiniteElementSpace pf, GridFunction gf) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParFiniteElementSpace pf, HypreParVector tv) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParMesh pmesh, GridFunction gf, int const * partitioning=None) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParMesh pmesh, GridFunction gf) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParMesh pmesh, std::istream & input) -> ParGridFunction
        __init__(mfem::ParGridFunction self, ParFiniteElementSpace fes, Vector v, int offset) -> ParGridFunction
        """

        from mfem._par.pmesh import ParMesh
        from mfem._par.pfespace import ParFiniteElementSpace
        from mfem._par.gridfunc import GridFunction
        if (len(args) == 2 and isinstance(args[1], str) and
             isinstance(args[0], ParMesh)):
            g0 = GridFunction(args[0], args[1])
            fec = g0.OwnFEC()
            fes = g0.FESpace()
            pfes = ParFiniteElementSpace(args[0], fec, fes.GetVDim(),
                                              fes.GetOrdering())
            x = ParGridFunction(pfes, g0)
            x.thisown = 0
            pfes.thisown = 0
            g0.thisown = 0
            self.this = x.this
            return 


        this = _pgridfunc.new_ParGridFunction(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
ParGridFunction_swigregister = _pgridfunc.ParGridFunction_swigregister
ParGridFunction_swigregister(ParGridFunction)


def L2ZZErrorEstimator(flux_integrator, x, smooth_flux_fes, flux_fes, errors, norm_p=2, solver_tol=1e-12, solver_max_it=200):
    """
    L2ZZErrorEstimator(BilinearFormIntegrator flux_integrator, ParGridFunction x, ParFiniteElementSpace smooth_flux_fes, ParFiniteElementSpace flux_fes, Vector errors, int norm_p=2, double solver_tol=1e-12, int solver_max_it=200) -> double
    L2ZZErrorEstimator(BilinearFormIntegrator flux_integrator, ParGridFunction x, ParFiniteElementSpace smooth_flux_fes, ParFiniteElementSpace flux_fes, Vector errors, int norm_p=2, double solver_tol=1e-12) -> double
    L2ZZErrorEstimator(BilinearFormIntegrator flux_integrator, ParGridFunction x, ParFiniteElementSpace smooth_flux_fes, ParFiniteElementSpace flux_fes, Vector errors, int norm_p=2) -> double
    L2ZZErrorEstimator(BilinearFormIntegrator flux_integrator, ParGridFunction x, ParFiniteElementSpace smooth_flux_fes, ParFiniteElementSpace flux_fes, Vector errors) -> double
    """
    return _pgridfunc.L2ZZErrorEstimator(flux_integrator, x, smooth_flux_fes, flux_fes, errors, norm_p, solver_tol, solver_max_it)
# This file is compatible with both classic and new-style classes.


