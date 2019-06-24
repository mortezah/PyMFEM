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
        mname = '.'.join((pkg, '_densemat')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_densemat')
    _densemat = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_densemat', [dirname(__file__)])
        except ImportError:
            import _densemat
            return _densemat
        try:
            _mod = imp.load_module('_densemat', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _densemat = swig_import_helper()
    del swig_import_helper
else:
    import _densemat
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


import mfem._ser.mem_manager
import mfem._ser.array
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
class DenseMatrix(mfem._ser.matrix.Matrix):
    """Proxy of C++ mfem::DenseMatrix class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DenseMatrix self) -> DenseMatrix
        __init__(mfem::DenseMatrix self, DenseMatrix arg2) -> DenseMatrix
        __init__(mfem::DenseMatrix self, int s) -> DenseMatrix
        __init__(mfem::DenseMatrix self, int m, int n) -> DenseMatrix
        __init__(mfem::DenseMatrix self, DenseMatrix mat, char ch) -> DenseMatrix
        __init__(mfem::DenseMatrix self, double * d, int h, int w) -> DenseMatrix
        """
        this = _densemat.new_DenseMatrix(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def UseExternalData(self, d, h, w):
        """UseExternalData(DenseMatrix self, double * d, int h, int w)"""
        return _densemat.DenseMatrix_UseExternalData(self, d, h, w)


    def Reset(self, d, h, w):
        """Reset(DenseMatrix self, double * d, int h, int w)"""
        return _densemat.DenseMatrix_Reset(self, d, h, w)


    def ClearExternalData(self):
        """ClearExternalData(DenseMatrix self)"""
        return _densemat.DenseMatrix_ClearExternalData(self)


    def Clear(self):
        """Clear(DenseMatrix self)"""
        return _densemat.DenseMatrix_Clear(self)


    def Size(self):
        """Size(DenseMatrix self) -> int"""
        return _densemat.DenseMatrix_Size(self)


    def SetSize(self, *args):
        """
        SetSize(DenseMatrix self, int s)
        SetSize(DenseMatrix self, int h, int w)
        """
        return _densemat.DenseMatrix_SetSize(self, *args)


    def Data(self):
        """Data(DenseMatrix self) -> double *"""
        return _densemat.DenseMatrix_Data(self)


    def GetData(self):
        """GetData(DenseMatrix self) -> double *"""
        return _densemat.DenseMatrix_GetData(self)


    def OwnsData(self):
        """OwnsData(DenseMatrix self) -> bool"""
        return _densemat.DenseMatrix_OwnsData(self)


    def __call__(self, *args):
        """
        __call__(DenseMatrix self, int i, int j) -> double
        __call__(DenseMatrix self, int i, int j) -> double const &
        """
        return _densemat.DenseMatrix___call__(self, *args)


    def __mul__(self, m):
        """__mul__(DenseMatrix self, DenseMatrix m) -> double"""
        return _densemat.DenseMatrix___mul__(self, m)


    def Trace(self):
        """Trace(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_Trace(self)


    def Elem(self, *args):
        """
        Elem(DenseMatrix self, int i, int j) -> double
        Elem(DenseMatrix self, int i, int j) -> double const &
        """
        return _densemat.DenseMatrix_Elem(self, *args)


    def Mult(self, *args):
        """
        Mult(DenseMatrix self, double const * x, double * y)
        Mult(DenseMatrix self, Vector x, Vector y)
        """
        return _densemat.DenseMatrix_Mult(self, *args)


    def MultTranspose(self, *args):
        """
        MultTranspose(DenseMatrix self, double const * x, double * y)
        MultTranspose(DenseMatrix self, Vector x, Vector y)
        """
        return _densemat.DenseMatrix_MultTranspose(self, *args)


    def AddMult(self, x, y):
        """AddMult(DenseMatrix self, Vector x, Vector y)"""
        return _densemat.DenseMatrix_AddMult(self, x, y)


    def AddMultTranspose(self, x, y):
        """AddMultTranspose(DenseMatrix self, Vector x, Vector y)"""
        return _densemat.DenseMatrix_AddMultTranspose(self, x, y)


    def AddMult_a(self, a, x, y):
        """AddMult_a(DenseMatrix self, double a, Vector x, Vector y)"""
        return _densemat.DenseMatrix_AddMult_a(self, a, x, y)


    def AddMultTranspose_a(self, a, x, y):
        """AddMultTranspose_a(DenseMatrix self, double a, Vector x, Vector y)"""
        return _densemat.DenseMatrix_AddMultTranspose_a(self, a, x, y)


    def LeftScaling(self, s):
        """LeftScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_LeftScaling(self, s)


    def InvLeftScaling(self, s):
        """InvLeftScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_InvLeftScaling(self, s)


    def RightScaling(self, s):
        """RightScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_RightScaling(self, s)


    def InvRightScaling(self, s):
        """InvRightScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_InvRightScaling(self, s)


    def SymmetricScaling(self, s):
        """SymmetricScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_SymmetricScaling(self, s)


    def InvSymmetricScaling(self, s):
        """InvSymmetricScaling(DenseMatrix self, Vector s)"""
        return _densemat.DenseMatrix_InvSymmetricScaling(self, s)


    def InnerProduct(self, *args):
        """
        InnerProduct(DenseMatrix self, double const * x, double const * y) -> double
        InnerProduct(DenseMatrix self, Vector x, Vector y) -> double
        """
        return _densemat.DenseMatrix_InnerProduct(self, *args)


    def Inverse(self):
        """Inverse(DenseMatrix self) -> MatrixInverse"""
        return _densemat.DenseMatrix_Inverse(self)


    def Invert(self):
        """Invert(DenseMatrix self)"""
        return _densemat.DenseMatrix_Invert(self)


    def SquareRootInverse(self):
        """SquareRootInverse(DenseMatrix self)"""
        return _densemat.DenseMatrix_SquareRootInverse(self)


    def Det(self):
        """Det(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_Det(self)


    def Weight(self):
        """Weight(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_Weight(self)


    def Set(self, *args):
        """
        Set(DenseMatrix self, double alpha, double const * A)
        Set(DenseMatrix self, double alpha, DenseMatrix A)
        """
        return _densemat.DenseMatrix_Set(self, *args)


    def Add(self, c, A):
        """Add(DenseMatrix self, double const c, DenseMatrix A)"""
        return _densemat.DenseMatrix_Add(self, c, A)


    def __iadd__(self, v):
        ret = _densmat.DenseMatrix___iadd__(self, v)
        ret.thisown = self.thisown
        self.thisown = 0                  
        return ret



    def __isub__(self, v):
        ret = _densmat.DenseMatrix___isub__(self, v)  
        ret.thisown = self.thisown
        self.thisown = 0            
        return ret



    def __imul__(self, v):
        ret = _densmat.DenseMatrix___imul__(self, v)  
        ret.thisown = self.thisown
        self.thisown = 0            
        return ret



    def Neg(self):
        """Neg(DenseMatrix self)"""
        return _densemat.DenseMatrix_Neg(self)


    def Norm2(self, v):
        """Norm2(DenseMatrix self, double * v)"""
        return _densemat.DenseMatrix_Norm2(self, v)


    def MaxMaxNorm(self):
        """MaxMaxNorm(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_MaxMaxNorm(self)


    def FNorm(self):
        """FNorm(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_FNorm(self)


    def FNorm2(self):
        """FNorm2(DenseMatrix self) -> double"""
        return _densemat.DenseMatrix_FNorm2(self)


    def Eigenvalues(self, *args):
        """
        Eigenvalues(DenseMatrix self, Vector ev)
        Eigenvalues(DenseMatrix self, Vector ev, DenseMatrix evect)
        Eigenvalues(DenseMatrix self, DenseMatrix b, Vector ev)
        Eigenvalues(DenseMatrix self, DenseMatrix b, Vector ev, DenseMatrix evect)
        """
        return _densemat.DenseMatrix_Eigenvalues(self, *args)


    def Eigensystem(self, *args):
        """
        Eigensystem(DenseMatrix self, Vector ev, DenseMatrix evect)
        Eigensystem(DenseMatrix self, DenseMatrix b, Vector ev, DenseMatrix evect)
        """
        return _densemat.DenseMatrix_Eigensystem(self, *args)


    def SingularValues(self, sv):
        """SingularValues(DenseMatrix self, Vector sv)"""
        return _densemat.DenseMatrix_SingularValues(self, sv)


    def Rank(self, tol):
        """Rank(DenseMatrix self, double tol) -> int"""
        return _densemat.DenseMatrix_Rank(self, tol)


    def CalcSingularvalue(self, i):
        """CalcSingularvalue(DenseMatrix self, int const i) -> double"""
        return _densemat.DenseMatrix_CalcSingularvalue(self, i)


    def CalcEigenvalues(self, arg2, vec):
        """CalcEigenvalues(DenseMatrix self, double * arg2, double * vec)"""
        return _densemat.DenseMatrix_CalcEigenvalues(self, arg2, vec)


    def GetRow(self, r, row):
        """GetRow(DenseMatrix self, int r, Vector row)"""
        return _densemat.DenseMatrix_GetRow(self, r, row)


    def GetColumn(self, *args):
        """
        GetColumn(DenseMatrix self, int c, Vector col)
        GetColumn(DenseMatrix self, int col) -> double
        GetColumn(DenseMatrix self, int col) -> double const *
        """
        return _densemat.DenseMatrix_GetColumn(self, *args)


    def GetColumnReference(self, c, col):
        """GetColumnReference(DenseMatrix self, int c, Vector col)"""
        return _densemat.DenseMatrix_GetColumnReference(self, c, col)


    def SetRow(self, *args):
        """
        SetRow(DenseMatrix self, int r, Vector row)
        SetRow(DenseMatrix self, int row, double value)
        """
        return _densemat.DenseMatrix_SetRow(self, *args)


    def SetCol(self, *args):
        """
        SetCol(DenseMatrix self, int c, Vector col)
        SetCol(DenseMatrix self, int col, double value)
        """
        return _densemat.DenseMatrix_SetCol(self, *args)


    def GetDiag(self, d):
        """GetDiag(DenseMatrix self, Vector d)"""
        return _densemat.DenseMatrix_GetDiag(self, d)


    def Getl1Diag(self, l):
        """Getl1Diag(DenseMatrix self, Vector l)"""
        return _densemat.DenseMatrix_Getl1Diag(self, l)


    def GetRowSums(self, l):
        """GetRowSums(DenseMatrix self, Vector l)"""
        return _densemat.DenseMatrix_GetRowSums(self, l)


    def Diag(self, *args):
        """
        Diag(DenseMatrix self, double c, int n)
        Diag(DenseMatrix self, double * diag, int n)
        """
        return _densemat.DenseMatrix_Diag(self, *args)


    def Transpose(self, *args):
        """
        Transpose(DenseMatrix self)
        Transpose(DenseMatrix self, DenseMatrix A)
        """
        return _densemat.DenseMatrix_Transpose(self, *args)


    def Symmetrize(self):
        """Symmetrize(DenseMatrix self)"""
        return _densemat.DenseMatrix_Symmetrize(self)


    def Lump(self):
        """Lump(DenseMatrix self)"""
        return _densemat.DenseMatrix_Lump(self)


    def GradToCurl(self, curl):
        """GradToCurl(DenseMatrix self, DenseMatrix curl)"""
        return _densemat.DenseMatrix_GradToCurl(self, curl)


    def GradToDiv(self, div):
        """GradToDiv(DenseMatrix self, Vector div)"""
        return _densemat.DenseMatrix_GradToDiv(self, div)


    def CopyRows(self, A, row1, row2):
        """CopyRows(DenseMatrix self, DenseMatrix A, int row1, int row2)"""
        return _densemat.DenseMatrix_CopyRows(self, A, row1, row2)


    def CopyCols(self, A, col1, col2):
        """CopyCols(DenseMatrix self, DenseMatrix A, int col1, int col2)"""
        return _densemat.DenseMatrix_CopyCols(self, A, col1, col2)


    def CopyMNt(self, A, row_offset, col_offset):
        """CopyMNt(DenseMatrix self, DenseMatrix A, int row_offset, int col_offset)"""
        return _densemat.DenseMatrix_CopyMNt(self, A, row_offset, col_offset)


    def CopyMN(self, *args):
        """
        CopyMN(DenseMatrix self, DenseMatrix A, int m, int n, int Aro, int Aco)
        CopyMN(DenseMatrix self, DenseMatrix A, int row_offset, int col_offset)
        CopyMN(DenseMatrix self, DenseMatrix A, int m, int n, int Aro, int Aco, int row_offset, int col_offset)
        """
        return _densemat.DenseMatrix_CopyMN(self, *args)


    def CopyMNDiag(self, *args):
        """
        CopyMNDiag(DenseMatrix self, double c, int n, int row_offset, int col_offset)
        CopyMNDiag(DenseMatrix self, double * diag, int n, int row_offset, int col_offset)
        """
        return _densemat.DenseMatrix_CopyMNDiag(self, *args)


    def CopyExceptMN(self, A, m, n):
        """CopyExceptMN(DenseMatrix self, DenseMatrix A, int m, int n)"""
        return _densemat.DenseMatrix_CopyExceptMN(self, A, m, n)


    def AddMatrix(self, *args):
        """
        AddMatrix(DenseMatrix self, DenseMatrix A, int ro, int co)
        AddMatrix(DenseMatrix self, double a, DenseMatrix A, int ro, int co)
        """
        return _densemat.DenseMatrix_AddMatrix(self, *args)


    def AddToVector(self, offset, v):
        """AddToVector(DenseMatrix self, int offset, Vector v)"""
        return _densemat.DenseMatrix_AddToVector(self, offset, v)


    def GetFromVector(self, offset, v):
        """GetFromVector(DenseMatrix self, int offset, Vector v)"""
        return _densemat.DenseMatrix_GetFromVector(self, offset, v)


    def AdjustDofDirection(self, dofs):
        """AdjustDofDirection(DenseMatrix self, intArray dofs)"""
        return _densemat.DenseMatrix_AdjustDofDirection(self, dofs)


    def Threshold(self, eps):
        """Threshold(DenseMatrix self, double eps)"""
        return _densemat.DenseMatrix_Threshold(self, eps)


    def CheckFinite(self):
        """CheckFinite(DenseMatrix self) -> int"""
        return _densemat.DenseMatrix_CheckFinite(self)


    def TestInversion(self):
        """TestInversion(DenseMatrix self)"""
        return _densemat.DenseMatrix_TestInversion(self)


    def MemoryUsage(self):
        """MemoryUsage(DenseMatrix self) -> long"""
        return _densemat.DenseMatrix_MemoryUsage(self)

    __swig_destroy__ = _densemat.delete_DenseMatrix
    __del__ = lambda self: None

    def Assign(self, *args):
        """
        Assign(DenseMatrix self, double const v)
        Assign(DenseMatrix self, DenseMatrix m)
        Assign(DenseMatrix self, PyObject * numpymat)
        """

        from numpy import ndarray, ascontiguousarray
        keep_link = False
        if len(args) == 1 and isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                     raise ValueError('Must be float64 array:' + args[0].dtype + ' was given')
                elif args[0].ndim != 2:
                    raise ValueError('Ndim must be two') 
                elif args[0].shape[1] != _densemat.DenseMatrix_Size(self):
                    raise ValueError('Length does not match')
                else:
                    args = (ascontiguousarray(args[0]),)


        val = _densemat.DenseMatrix_Assign(self, *args)

        return self


        return val


    def __getitem__(self, *args):
        i, j = args[0][0], args[0][1]
        return _densemat.DenseMatrix___getitem__(self, i, j)



    def __setitem__(self, *args):
        i, j, v = args[0][0], args[0][1], args[1]
        return _densemat.DenseMatrix___setitem__(self, i, j, v)



    def GetDataArray(self):
        """GetDataArray(DenseMatrix self) -> PyObject *"""
        return _densemat.DenseMatrix_GetDataArray(self)


    def Print(self, *args):
        """
        Print(DenseMatrix self, std::ostream & out, int width_=4)
        Print(DenseMatrix self, std::ostream & out)
        Print(DenseMatrix self)
        Print(DenseMatrix self, char const * file, int precision=8)
        Print(DenseMatrix self, char const * file)
        """
        return _densemat.DenseMatrix_Print(self, *args)


    def PrintT(self, *args):
        """
        PrintT(DenseMatrix self, std::ostream & out, int width_=4)
        PrintT(DenseMatrix self, std::ostream & out)
        PrintT(DenseMatrix self)
        PrintT(DenseMatrix self, char const * file, int precision=8)
        PrintT(DenseMatrix self, char const * file)
        """
        return _densemat.DenseMatrix_PrintT(self, *args)


    def PrintMatlab(self, *args):
        """
        PrintMatlab(DenseMatrix self, std::ostream & out)
        PrintMatlab(DenseMatrix self)
        PrintMatlab(DenseMatrix self, char const * file, int precision=8)
        PrintMatlab(DenseMatrix self, char const * file)
        """
        return _densemat.DenseMatrix_PrintMatlab(self, *args)

DenseMatrix_swigregister = _densemat.DenseMatrix_swigregister
DenseMatrix_swigregister(DenseMatrix)


def AddMult(b, c, a):
    """AddMult(DenseMatrix b, DenseMatrix c, DenseMatrix a)"""
    return _densemat.AddMult(b, c, a)

def CalcAdjugate(a, adja):
    """CalcAdjugate(DenseMatrix a, DenseMatrix adja)"""
    return _densemat.CalcAdjugate(a, adja)

def CalcAdjugateTranspose(a, adjat):
    """CalcAdjugateTranspose(DenseMatrix a, DenseMatrix adjat)"""
    return _densemat.CalcAdjugateTranspose(a, adjat)

def CalcInverse(a, inva):
    """CalcInverse(DenseMatrix a, DenseMatrix inva)"""
    return _densemat.CalcInverse(a, inva)

def CalcInverseTranspose(a, inva):
    """CalcInverseTranspose(DenseMatrix a, DenseMatrix inva)"""
    return _densemat.CalcInverseTranspose(a, inva)

def CalcOrtho(J, n):
    """CalcOrtho(DenseMatrix J, Vector n)"""
    return _densemat.CalcOrtho(J, n)

def MultAAt(a, aat):
    """MultAAt(DenseMatrix a, DenseMatrix aat)"""
    return _densemat.MultAAt(a, aat)

def MultADAt(A, D, ADAt):
    """MultADAt(DenseMatrix A, Vector D, DenseMatrix ADAt)"""
    return _densemat.MultADAt(A, D, ADAt)

def AddMultADAt(A, D, ADAt):
    """AddMultADAt(DenseMatrix A, Vector D, DenseMatrix ADAt)"""
    return _densemat.AddMultADAt(A, D, ADAt)

def MultABt(A, B, ABt):
    """MultABt(DenseMatrix A, DenseMatrix B, DenseMatrix ABt)"""
    return _densemat.MultABt(A, B, ABt)

def MultADBt(A, D, B, ADBt):
    """MultADBt(DenseMatrix A, Vector D, DenseMatrix B, DenseMatrix ADBt)"""
    return _densemat.MultADBt(A, D, B, ADBt)

def AddMultABt(A, B, ABt):
    """AddMultABt(DenseMatrix A, DenseMatrix B, DenseMatrix ABt)"""
    return _densemat.AddMultABt(A, B, ABt)

def AddMultADBt(A, D, B, ADBt):
    """AddMultADBt(DenseMatrix A, Vector D, DenseMatrix B, DenseMatrix ADBt)"""
    return _densemat.AddMultADBt(A, D, B, ADBt)

def AddMult_a_ABt(a, A, B, ABt):
    """AddMult_a_ABt(double a, DenseMatrix A, DenseMatrix B, DenseMatrix ABt)"""
    return _densemat.AddMult_a_ABt(a, A, B, ABt)

def MultAtB(A, B, AtB):
    """MultAtB(DenseMatrix A, DenseMatrix B, DenseMatrix AtB)"""
    return _densemat.MultAtB(A, B, AtB)

def AddMult_a_AAt(a, A, AAt):
    """AddMult_a_AAt(double a, DenseMatrix A, DenseMatrix AAt)"""
    return _densemat.AddMult_a_AAt(a, A, AAt)

def Mult_a_AAt(a, A, AAt):
    """Mult_a_AAt(double a, DenseMatrix A, DenseMatrix AAt)"""
    return _densemat.Mult_a_AAt(a, A, AAt)

def MultVVt(v, vvt):
    """MultVVt(Vector v, DenseMatrix vvt)"""
    return _densemat.MultVVt(v, vvt)

def MultVWt(v, w, VWt):
    """MultVWt(Vector v, Vector w, DenseMatrix VWt)"""
    return _densemat.MultVWt(v, w, VWt)

def AddMultVWt(v, w, VWt):
    """AddMultVWt(Vector v, Vector w, DenseMatrix VWt)"""
    return _densemat.AddMultVWt(v, w, VWt)

def AddMultVVt(v, VWt):
    """AddMultVVt(Vector v, DenseMatrix VWt)"""
    return _densemat.AddMultVVt(v, VWt)

def AddMult_a_VWt(a, v, w, VWt):
    """AddMult_a_VWt(double const a, Vector v, Vector w, DenseMatrix VWt)"""
    return _densemat.AddMult_a_VWt(a, v, w, VWt)

def AddMult_a_VVt(a, v, VVt):
    """AddMult_a_VVt(double const a, Vector v, DenseMatrix VVt)"""
    return _densemat.AddMult_a_VVt(a, v, VVt)
class LUFactors(_object):
    """Proxy of C++ mfem::LUFactors class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LUFactors, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LUFactors, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _densemat.LUFactors_data_set
    __swig_getmethods__["data"] = _densemat.LUFactors_data_get
    if _newclass:
        data = _swig_property(_densemat.LUFactors_data_get, _densemat.LUFactors_data_set)
    __swig_setmethods__["ipiv"] = _densemat.LUFactors_ipiv_set
    __swig_getmethods__["ipiv"] = _densemat.LUFactors_ipiv_get
    if _newclass:
        ipiv = _swig_property(_densemat.LUFactors_ipiv_get, _densemat.LUFactors_ipiv_set)
    ipiv_base = _densemat.LUFactors_ipiv_base

    def __init__(self, *args):
        """
        __init__(mfem::LUFactors self) -> LUFactors
        __init__(mfem::LUFactors self, double * data_, int * ipiv_) -> LUFactors
        """
        this = _densemat.new_LUFactors(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Factor(self, m):
        """Factor(LUFactors self, int m)"""
        return _densemat.LUFactors_Factor(self, m)


    def Det(self, m):
        """Det(LUFactors self, int m) -> double"""
        return _densemat.LUFactors_Det(self, m)


    def Mult(self, m, n, X):
        """Mult(LUFactors self, int m, int n, double * X)"""
        return _densemat.LUFactors_Mult(self, m, n, X)


    def LSolve(self, m, n, X):
        """LSolve(LUFactors self, int m, int n, double * X)"""
        return _densemat.LUFactors_LSolve(self, m, n, X)


    def USolve(self, m, n, X):
        """USolve(LUFactors self, int m, int n, double * X)"""
        return _densemat.LUFactors_USolve(self, m, n, X)


    def Solve(self, m, n, X):
        """Solve(LUFactors self, int m, int n, double * X)"""
        return _densemat.LUFactors_Solve(self, m, n, X)


    def GetInverseMatrix(self, m, X):
        """GetInverseMatrix(LUFactors self, int m, double * X)"""
        return _densemat.LUFactors_GetInverseMatrix(self, m, X)


    def SubMult(m, n, r, A21, X1, X2):
        """SubMult(int m, int n, int r, double const * A21, double const * X1, double * X2)"""
        return _densemat.LUFactors_SubMult(m, n, r, A21, X1, X2)

    SubMult = staticmethod(SubMult)

    def BlockFactor(self, m, n, A12, A21, A22):
        """BlockFactor(LUFactors self, int m, int n, double * A12, double * A21, double * A22)"""
        return _densemat.LUFactors_BlockFactor(self, m, n, A12, A21, A22)


    def BlockForwSolve(self, m, n, r, L21, B1, B2):
        """BlockForwSolve(LUFactors self, int m, int n, int r, double const * L21, double * B1, double * B2)"""
        return _densemat.LUFactors_BlockForwSolve(self, m, n, r, L21, B1, B2)


    def BlockBackSolve(self, m, n, r, U12, X2, Y1):
        """BlockBackSolve(LUFactors self, int m, int n, int r, double const * U12, double const * X2, double * Y1)"""
        return _densemat.LUFactors_BlockBackSolve(self, m, n, r, U12, X2, Y1)

    __swig_destroy__ = _densemat.delete_LUFactors
    __del__ = lambda self: None
LUFactors_swigregister = _densemat.LUFactors_swigregister
LUFactors_swigregister(LUFactors)

def LUFactors_SubMult(m, n, r, A21, X1, X2):
    """LUFactors_SubMult(int m, int n, int r, double const * A21, double const * X1, double * X2)"""
    return _densemat.LUFactors_SubMult(m, n, r, A21, X1, X2)

class DenseMatrixInverse(mfem._ser.matrix.MatrixInverse):
    """Proxy of C++ mfem::DenseMatrixInverse class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.MatrixInverse]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixInverse, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.MatrixInverse]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixInverse, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DenseMatrixInverse self) -> DenseMatrixInverse
        __init__(mfem::DenseMatrixInverse self, DenseMatrix mat) -> DenseMatrixInverse
        __init__(mfem::DenseMatrixInverse self, DenseMatrix mat) -> DenseMatrixInverse
        """
        this = _densemat.new_DenseMatrixInverse(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Size(self):
        """Size(DenseMatrixInverse self) -> int"""
        return _densemat.DenseMatrixInverse_Size(self)


    def Factor(self, *args):
        """
        Factor(DenseMatrixInverse self)
        Factor(DenseMatrixInverse self, DenseMatrix mat)
        """
        return _densemat.DenseMatrixInverse_Factor(self, *args)


    def SetOperator(self, op):
        """SetOperator(DenseMatrixInverse self, Operator op)"""
        return _densemat.DenseMatrixInverse_SetOperator(self, op)


    def Mult(self, *args):
        """
        Mult(DenseMatrixInverse self, Vector x, Vector y)
        Mult(DenseMatrixInverse self, DenseMatrix B, DenseMatrix X)
        Mult(DenseMatrixInverse self, DenseMatrix X)
        """
        return _densemat.DenseMatrixInverse_Mult(self, *args)


    def GetInverseMatrix(self, Ainv):
        """GetInverseMatrix(DenseMatrixInverse self, DenseMatrix Ainv)"""
        return _densemat.DenseMatrixInverse_GetInverseMatrix(self, Ainv)


    def Det(self):
        """Det(DenseMatrixInverse self) -> double"""
        return _densemat.DenseMatrixInverse_Det(self)


    def TestInversion(self):
        """TestInversion(DenseMatrixInverse self)"""
        return _densemat.DenseMatrixInverse_TestInversion(self)

    __swig_destroy__ = _densemat.delete_DenseMatrixInverse
    __del__ = lambda self: None
DenseMatrixInverse_swigregister = _densemat.DenseMatrixInverse_swigregister
DenseMatrixInverse_swigregister(DenseMatrixInverse)

class DenseMatrixEigensystem(_object):
    """Proxy of C++ mfem::DenseMatrixEigensystem class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixEigensystem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixEigensystem, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DenseMatrixEigensystem self, DenseMatrix m) -> DenseMatrixEigensystem
        __init__(mfem::DenseMatrixEigensystem self, DenseMatrixEigensystem other) -> DenseMatrixEigensystem
        """
        this = _densemat.new_DenseMatrixEigensystem(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self):
        """Eval(DenseMatrixEigensystem self)"""
        return _densemat.DenseMatrixEigensystem_Eval(self)


    def Eigenvalues(self):
        """Eigenvalues(DenseMatrixEigensystem self) -> Vector"""
        return _densemat.DenseMatrixEigensystem_Eigenvalues(self)


    def Eigenvectors(self):
        """Eigenvectors(DenseMatrixEigensystem self) -> DenseMatrix"""
        return _densemat.DenseMatrixEigensystem_Eigenvectors(self)


    def Eigenvalue(self, i):
        """Eigenvalue(DenseMatrixEigensystem self, int i) -> double"""
        return _densemat.DenseMatrixEigensystem_Eigenvalue(self, i)


    def Eigenvector(self, i):
        """Eigenvector(DenseMatrixEigensystem self, int i) -> Vector"""
        return _densemat.DenseMatrixEigensystem_Eigenvector(self, i)

    __swig_destroy__ = _densemat.delete_DenseMatrixEigensystem
    __del__ = lambda self: None
DenseMatrixEigensystem_swigregister = _densemat.DenseMatrixEigensystem_swigregister
DenseMatrixEigensystem_swigregister(DenseMatrixEigensystem)

class DenseMatrixSVD(_object):
    """Proxy of C++ mfem::DenseMatrixSVD class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseMatrixSVD, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseMatrixSVD, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DenseMatrixSVD self, DenseMatrix M) -> DenseMatrixSVD
        __init__(mfem::DenseMatrixSVD self, int h, int w) -> DenseMatrixSVD
        """
        this = _densemat.new_DenseMatrixSVD(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, M):
        """Eval(DenseMatrixSVD self, DenseMatrix M)"""
        return _densemat.DenseMatrixSVD_Eval(self, M)


    def Singularvalues(self):
        """Singularvalues(DenseMatrixSVD self) -> Vector"""
        return _densemat.DenseMatrixSVD_Singularvalues(self)


    def Singularvalue(self, i):
        """Singularvalue(DenseMatrixSVD self, int i) -> double"""
        return _densemat.DenseMatrixSVD_Singularvalue(self, i)

    __swig_destroy__ = _densemat.delete_DenseMatrixSVD
    __del__ = lambda self: None
DenseMatrixSVD_swigregister = _densemat.DenseMatrixSVD_swigregister
DenseMatrixSVD_swigregister(DenseMatrixSVD)

class DenseTensor(_object):
    """Proxy of C++ mfem::DenseTensor class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DenseTensor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DenseTensor, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DenseTensor self) -> DenseTensor
        __init__(mfem::DenseTensor self, int i, int j, int k) -> DenseTensor
        __init__(mfem::DenseTensor self, DenseTensor other) -> DenseTensor
        """
        this = _densemat.new_DenseTensor(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SizeI(self):
        """SizeI(DenseTensor self) -> int"""
        return _densemat.DenseTensor_SizeI(self)


    def SizeJ(self):
        """SizeJ(DenseTensor self) -> int"""
        return _densemat.DenseTensor_SizeJ(self)


    def SizeK(self):
        """SizeK(DenseTensor self) -> int"""
        return _densemat.DenseTensor_SizeK(self)


    def TotalSize(self):
        """TotalSize(DenseTensor self) -> int"""
        return _densemat.DenseTensor_TotalSize(self)


    def SetSize(self, i, j, k):
        """SetSize(DenseTensor self, int i, int j, int k)"""
        return _densemat.DenseTensor_SetSize(self, i, j, k)


    def UseExternalData(self, ext_data, i, j, k):
        """UseExternalData(DenseTensor self, double * ext_data, int i, int j, int k)"""
        return _densemat.DenseTensor_UseExternalData(self, ext_data, i, j, k)


    def __call__(self, *args):
        """
        __call__(DenseTensor self, int k) -> DenseMatrix
        __call__(DenseTensor self, int k) -> DenseMatrix
        __call__(DenseTensor self, int i, int j, int k) -> double
        __call__(DenseTensor self, int i, int j, int k) -> double const &
        """
        return _densemat.DenseTensor___call__(self, *args)


    def GetData(self, k):
        """GetData(DenseTensor self, int k) -> double *"""
        return _densemat.DenseTensor_GetData(self, k)


    def Data(self, *args):
        """
        Data(DenseTensor self) -> double
        Data(DenseTensor self) -> double const *
        """
        return _densemat.DenseTensor_Data(self, *args)


    def GetMemory(self, *args):
        """
        GetMemory(DenseTensor self) -> mfem::Memory< double >
        GetMemory(DenseTensor self) -> mfem::Memory< double > const &
        """
        return _densemat.DenseTensor_GetMemory(self, *args)


    def AddMult(self, elem_dof, x, y):
        """AddMult(DenseTensor self, mfem::Table const & elem_dof, Vector x, Vector y)"""
        return _densemat.DenseTensor_AddMult(self, elem_dof, x, y)


    def Clear(self):
        """Clear(DenseTensor self)"""
        return _densemat.DenseTensor_Clear(self)


    def MemoryUsage(self):
        """MemoryUsage(DenseTensor self) -> long"""
        return _densemat.DenseTensor_MemoryUsage(self)

    __swig_destroy__ = _densemat.delete_DenseTensor
    __del__ = lambda self: None

    def Assign(self, c):
        """Assign(DenseTensor self, double const c)"""
        val = _densemat.DenseTensor_Assign(self, c)

        return self


        return val


    def __getitem__(self, *args):
      try:
         check = len(args[0]) == 3
      except:
         check = False
      if check:
         i, j, k = args[0][0], args[0][1], args[0][2]
         return _densemat.DenseTensor___getitem__(self, i, j, k)
      try:
         check = int(args[0])
      except:
         check = -1
      if check >= 0:     
         return _densemat.DenseTensor___getitem__(self, check)



    def __setitem__(self, *args):
        i, j, k, v = args[0][0], args[0][1], args[0][2], args[1]
        return _densemat.DenseTensor___setitem__(self, i, j, k, v)



    def GetDataArray(self):
        """GetDataArray(DenseTensor self) -> PyObject *"""
        return _densemat.DenseTensor_GetDataArray(self)

DenseTensor_swigregister = _densemat.DenseTensor_swigregister
DenseTensor_swigregister(DenseTensor)

# This file is compatible with both classic and new-style classes.


