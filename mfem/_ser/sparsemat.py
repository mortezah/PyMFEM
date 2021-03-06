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
        mname = '.'.join((pkg, '_sparsemat')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sparsemat')
    _sparsemat = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sparsemat', [dirname(__file__)])
        except ImportError:
            import _sparsemat
            return _sparsemat
        try:
            _mod = imp.load_module('_sparsemat', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _sparsemat = swig_import_helper()
    del swig_import_helper
else:
    import _sparsemat
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


import mfem._ser.array
import mfem._ser.ostream_typemap
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.densemat

def RAP_P(A, R, ORAP):
    """RAP_P(SparseMatrix A, SparseMatrix R, SparseMatrix ORAP) -> SparseMatrix"""
    return _sparsemat.RAP_P(A, R, ORAP)

def RAP_R(Rt, A, P):
    """RAP_R(SparseMatrix Rt, SparseMatrix A, SparseMatrix P) -> SparseMatrix"""
    return _sparsemat.RAP_R(Rt, A, P)
class RowNode(_object):
    """Proxy of C++ mfem::RowNode class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RowNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RowNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Value"] = _sparsemat.RowNode_Value_set
    __swig_getmethods__["Value"] = _sparsemat.RowNode_Value_get
    if _newclass:
        Value = _swig_property(_sparsemat.RowNode_Value_get, _sparsemat.RowNode_Value_set)
    __swig_setmethods__["Prev"] = _sparsemat.RowNode_Prev_set
    __swig_getmethods__["Prev"] = _sparsemat.RowNode_Prev_get
    if _newclass:
        Prev = _swig_property(_sparsemat.RowNode_Prev_get, _sparsemat.RowNode_Prev_set)
    __swig_setmethods__["Column"] = _sparsemat.RowNode_Column_set
    __swig_getmethods__["Column"] = _sparsemat.RowNode_Column_get
    if _newclass:
        Column = _swig_property(_sparsemat.RowNode_Column_get, _sparsemat.RowNode_Column_set)

    def __init__(self):
        """__init__(mfem::RowNode self) -> RowNode"""
        this = _sparsemat.new_RowNode()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _sparsemat.delete_RowNode
    __del__ = lambda self: None
RowNode_swigregister = _sparsemat.RowNode_swigregister
RowNode_swigregister(RowNode)

class SparseMatrix(mfem._ser.matrix.AbstractSparseMatrix):
    """Proxy of C++ mfem::SparseMatrix class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.AbstractSparseMatrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.AbstractSparseMatrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::SparseMatrix self) -> SparseMatrix
        __init__(mfem::SparseMatrix self, int nrows, int ncols=-1) -> SparseMatrix
        __init__(mfem::SparseMatrix self, int nrows) -> SparseMatrix
        __init__(mfem::SparseMatrix self, int * i) -> SparseMatrix
        __init__(mfem::SparseMatrix self, int * i, bool ownij, bool owna, bool issorted) -> SparseMatrix
        __init__(mfem::SparseMatrix self, int nrows, int ncols, int rowsize) -> SparseMatrix
        __init__(mfem::SparseMatrix self, SparseMatrix mat, bool copy_graph=True) -> SparseMatrix
        __init__(mfem::SparseMatrix self, SparseMatrix mat) -> SparseMatrix
        """

        import numpy as np  
        from scipy.sparse import csr_matrix
        if len(args) == 1 and isinstance(args[0], csr_matrix):
           csr = args[0]
           if np.real(csr).dtype != 'float64':
               csr = csr.astype('float64')
           i = np.ascontiguousarray(csr.indptr)
           j = np.ascontiguousarray(csr.indices)
           data = np.ascontiguousarray(csr.data)
           m, n = csr.shape
           this = _sparsemat.new_SparseMatrix([i, j, data, m, n])
           try:
               self.this.append(this)
           except __builtin__.Exception:
               self.this = this
           _sparsemat.SparseMatrix_SetGraphOwner(self, False)
           _sparsemat.SparseMatrix_SetDataOwner(self, False)
           self._i_data = i
           self._j_data = j
           self._d_data = data

           return


        this = _sparsemat.new_SparseMatrix(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def MakeRef(self, master):
        """MakeRef(SparseMatrix self, SparseMatrix master)"""
        return _sparsemat.SparseMatrix_MakeRef(self, master)


    def Size(self):
        """Size(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_Size(self)


    def Clear(self):
        """Clear(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_Clear(self)


    def Empty(self):
        """Empty(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_Empty(self)


    def GetI(self):
        """GetI(SparseMatrix self) -> int *"""
        return _sparsemat.SparseMatrix_GetI(self)


    def GetJ(self):
        """GetJ(SparseMatrix self) -> int *"""
        return _sparsemat.SparseMatrix_GetJ(self)


    def GetData(self):
        """GetData(SparseMatrix self) -> double *"""
        return _sparsemat.SparseMatrix_GetData(self)


    def RowSize(self, i):
        """RowSize(SparseMatrix self, int const i) -> int"""
        return _sparsemat.SparseMatrix_RowSize(self, i)


    def MaxRowSize(self):
        """MaxRowSize(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_MaxRowSize(self)


    def GetRowColumns(self, *args):
        """
        GetRowColumns(SparseMatrix self, int const row) -> int
        GetRowColumns(SparseMatrix self, int const row) -> int const *
        """
        return _sparsemat.SparseMatrix_GetRowColumns(self, *args)


    def GetRowEntries(self, *args):
        """
        GetRowEntries(SparseMatrix self, int const row) -> double
        GetRowEntries(SparseMatrix self, int const row) -> double const *
        """
        return _sparsemat.SparseMatrix_GetRowEntries(self, *args)


    def SetWidth(self, width_=-1):
        """
        SetWidth(SparseMatrix self, int width_=-1)
        SetWidth(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_SetWidth(self, width_)


    def ActualWidth(self):
        """ActualWidth(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_ActualWidth(self)


    def SortColumnIndices(self):
        """SortColumnIndices(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_SortColumnIndices(self)


    def MoveDiagonalFirst(self):
        """MoveDiagonalFirst(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_MoveDiagonalFirst(self)


    def Elem(self, *args):
        """
        Elem(SparseMatrix self, int i, int j) -> double
        Elem(SparseMatrix self, int i, int j) -> double const &
        """
        return _sparsemat.SparseMatrix_Elem(self, *args)


    def __call__(self, *args):
        """
        __call__(SparseMatrix self, int i, int j) -> double
        __call__(SparseMatrix self, int i, int j) -> double const &
        """
        return _sparsemat.SparseMatrix___call__(self, *args)


    def GetDiag(self, d):
        """GetDiag(SparseMatrix self, Vector d)"""
        return _sparsemat.SparseMatrix_GetDiag(self, d)


    def Mult(self, x, y):
        """Mult(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Mult(self, x, y)


    def AddMult(self, x, y, a=1.0):
        """
        AddMult(SparseMatrix self, Vector x, Vector y, double const a=1.0)
        AddMult(SparseMatrix self, Vector x, Vector y)
        """
        return _sparsemat.SparseMatrix_AddMult(self, x, y, a)


    def MultTranspose(self, x, y):
        """MultTranspose(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_MultTranspose(self, x, y)


    def AddMultTranspose(self, x, y, a=1.0):
        """
        AddMultTranspose(SparseMatrix self, Vector x, Vector y, double const a=1.0)
        AddMultTranspose(SparseMatrix self, Vector x, Vector y)
        """
        return _sparsemat.SparseMatrix_AddMultTranspose(self, x, y, a)


    def PartMult(self, rows, x, y):
        """PartMult(SparseMatrix self, intArray rows, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_PartMult(self, rows, x, y)


    def PartAddMult(self, rows, x, y, a=1.0):
        """
        PartAddMult(SparseMatrix self, intArray rows, Vector x, Vector y, double const a=1.0)
        PartAddMult(SparseMatrix self, intArray rows, Vector x, Vector y)
        """
        return _sparsemat.SparseMatrix_PartAddMult(self, rows, x, y, a)


    def BooleanMult(self, x, y):
        """BooleanMult(SparseMatrix self, intArray x, intArray y)"""
        return _sparsemat.SparseMatrix_BooleanMult(self, x, y)


    def BooleanMultTranspose(self, x, y):
        """BooleanMultTranspose(SparseMatrix self, intArray x, intArray y)"""
        return _sparsemat.SparseMatrix_BooleanMultTranspose(self, x, y)


    def InnerProduct(self, x, y):
        """InnerProduct(SparseMatrix self, Vector x, Vector y) -> double"""
        return _sparsemat.SparseMatrix_InnerProduct(self, x, y)


    def GetRowSums(self, x):
        """GetRowSums(SparseMatrix self, Vector x)"""
        return _sparsemat.SparseMatrix_GetRowSums(self, x)


    def GetRowNorml1(self, irow):
        """GetRowNorml1(SparseMatrix self, int irow) -> double"""
        return _sparsemat.SparseMatrix_GetRowNorml1(self, irow)


    def Inverse(self):
        """Inverse(SparseMatrix self) -> MatrixInverse"""
        return _sparsemat.SparseMatrix_Inverse(self)


    def EliminateRow(self, *args):
        """
        EliminateRow(SparseMatrix self, int row, double const sol, Vector rhs)
        EliminateRow(SparseMatrix self, int row, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRow(SparseMatrix self, int row)
        """
        return _sparsemat.SparseMatrix_EliminateRow(self, *args)


    def EliminateCol(self, *args):
        """
        EliminateCol(SparseMatrix self, int col, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateCol(SparseMatrix self, int col)
        """
        return _sparsemat.SparseMatrix_EliminateCol(self, *args)


    def EliminateCols(self, cols, x=None, b=None):
        """
        EliminateCols(SparseMatrix self, intArray cols, Vector x=None, Vector b=None)
        EliminateCols(SparseMatrix self, intArray cols, Vector x=None)
        EliminateCols(SparseMatrix self, intArray cols)
        """
        return _sparsemat.SparseMatrix_EliminateCols(self, cols, x, b)


    def EliminateRowColMultipleRHS(self, *args):
        """
        EliminateRowColMultipleRHS(SparseMatrix self, int rc, Vector sol, DenseMatrix rhs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRowColMultipleRHS(SparseMatrix self, int rc, Vector sol, DenseMatrix rhs)
        """
        return _sparsemat.SparseMatrix_EliminateRowColMultipleRHS(self, *args)


    def EliminateRowColDiag(self, rc, value):
        """EliminateRowColDiag(SparseMatrix self, int rc, double value)"""
        return _sparsemat.SparseMatrix_EliminateRowColDiag(self, rc, value)


    def EliminateRowCol(self, *args):
        """
        EliminateRowCol(SparseMatrix self, int rc, double const sol, Vector rhs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRowCol(SparseMatrix self, int rc, double const sol, Vector rhs)
        EliminateRowCol(SparseMatrix self, int rc, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRowCol(SparseMatrix self, int rc)
        EliminateRowCol(SparseMatrix self, int rc, SparseMatrix Ae, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRowCol(SparseMatrix self, int rc, SparseMatrix Ae)
        """
        return _sparsemat.SparseMatrix_EliminateRowCol(self, *args)


    def SetDiagIdentity(self):
        """SetDiagIdentity(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_SetDiagIdentity(self)


    def EliminateZeroRows(self, threshold=1e-12):
        """
        EliminateZeroRows(SparseMatrix self, double const threshold=1e-12)
        EliminateZeroRows(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_EliminateZeroRows(self, threshold)


    def Gauss_Seidel_forw(self, x, y):
        """Gauss_Seidel_forw(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Gauss_Seidel_forw(self, x, y)


    def Gauss_Seidel_back(self, x, y):
        """Gauss_Seidel_back(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Gauss_Seidel_back(self, x, y)


    def GetJacobiScaling(self):
        """GetJacobiScaling(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_GetJacobiScaling(self)


    def Jacobi(self, b, x0, x1, sc):
        """Jacobi(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc)"""
        return _sparsemat.SparseMatrix_Jacobi(self, b, x0, x1, sc)


    def DiagScale(self, b, x, sc=1.0):
        """
        DiagScale(SparseMatrix self, Vector b, Vector x, double sc=1.0)
        DiagScale(SparseMatrix self, Vector b, Vector x)
        """
        return _sparsemat.SparseMatrix_DiagScale(self, b, x, sc)


    def Jacobi2(self, b, x0, x1, sc=1.0):
        """
        Jacobi2(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc=1.0)
        Jacobi2(SparseMatrix self, Vector b, Vector x0, Vector x1)
        """
        return _sparsemat.SparseMatrix_Jacobi2(self, b, x0, x1, sc)


    def Jacobi3(self, b, x0, x1, sc=1.0):
        """
        Jacobi3(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc=1.0)
        Jacobi3(SparseMatrix self, Vector b, Vector x0, Vector x1)
        """
        return _sparsemat.SparseMatrix_Jacobi3(self, b, x0, x1, sc)


    def Finalize(self, *args):
        """
        Finalize(SparseMatrix self, int skip_zeros=1)
        Finalize(SparseMatrix self)
        Finalize(SparseMatrix self, int skip_zeros, bool fix_empty_rows)
        """
        return _sparsemat.SparseMatrix_Finalize(self, *args)


    def Finalized(self):
        """Finalized(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_Finalized(self)


    def areColumnsSorted(self):
        """areColumnsSorted(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_areColumnsSorted(self)


    def GetBlocks(self, blocks):
        """GetBlocks(SparseMatrix self, mfem::Array2D< mfem::SparseMatrix * > & blocks)"""
        return _sparsemat.SparseMatrix_GetBlocks(self, blocks)


    def GetSubMatrix(self, rows, cols, subm):
        """GetSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm)"""
        return _sparsemat.SparseMatrix_GetSubMatrix(self, rows, cols, subm)


    def SetColPtr(self, row):
        """SetColPtr(SparseMatrix self, int const row)"""
        return _sparsemat.SparseMatrix_SetColPtr(self, row)


    def ClearColPtr(self):
        """ClearColPtr(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_ClearColPtr(self)


    def _Get_(self, col):
        """_Get_(SparseMatrix self, int const col) -> double"""
        return _sparsemat.SparseMatrix__Get_(self, col)


    def SearchRow(self, *args):
        """
        SearchRow(SparseMatrix self, int const col) -> double
        SearchRow(SparseMatrix self, int const row, int const col) -> double &
        """
        return _sparsemat.SparseMatrix_SearchRow(self, *args)


    def _Add_(self, *args):
        """
        _Add_(SparseMatrix self, int const col, double const a)
        _Add_(SparseMatrix self, int const row, int const col, double const a)
        """
        return _sparsemat.SparseMatrix__Add_(self, *args)


    def _Set_(self, *args):
        """
        _Set_(SparseMatrix self, int const col, double const a)
        _Set_(SparseMatrix self, int const row, int const col, double const a)
        """
        return _sparsemat.SparseMatrix__Set_(self, *args)


    def Set(self, i, j, a):
        """Set(SparseMatrix self, int const i, int const j, double const a)"""
        return _sparsemat.SparseMatrix_Set(self, i, j, a)


    def SetSubMatrix(self, rows, cols, subm, skip_zeros=1):
        """
        SetSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)
        SetSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm)
        """
        return _sparsemat.SparseMatrix_SetSubMatrix(self, rows, cols, subm, skip_zeros)


    def SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros=1):
        """
        SetSubMatrixTranspose(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)
        SetSubMatrixTranspose(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm)
        """
        return _sparsemat.SparseMatrix_SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros)


    def AddSubMatrix(self, rows, cols, subm, skip_zeros=1):
        """
        AddSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)
        AddSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm)
        """
        return _sparsemat.SparseMatrix_AddSubMatrix(self, rows, cols, subm, skip_zeros)


    def RowIsEmpty(self, row):
        """RowIsEmpty(SparseMatrix self, int const row) -> bool"""
        return _sparsemat.SparseMatrix_RowIsEmpty(self, row)


    def GetRow(self, row, cols, srow):
        """GetRow(SparseMatrix self, int const row, intArray cols, Vector srow) -> int"""
        return _sparsemat.SparseMatrix_GetRow(self, row, cols, srow)


    def SetRow(self, row, cols, srow):
        """SetRow(SparseMatrix self, int const row, intArray cols, Vector srow)"""
        return _sparsemat.SparseMatrix_SetRow(self, row, cols, srow)


    def AddRow(self, row, cols, srow):
        """AddRow(SparseMatrix self, int const row, intArray cols, Vector srow)"""
        return _sparsemat.SparseMatrix_AddRow(self, row, cols, srow)


    def ScaleRow(self, row, scale):
        """ScaleRow(SparseMatrix self, int const row, double const scale)"""
        return _sparsemat.SparseMatrix_ScaleRow(self, row, scale)


    def ScaleRows(self, sl):
        """ScaleRows(SparseMatrix self, Vector sl)"""
        return _sparsemat.SparseMatrix_ScaleRows(self, sl)


    def ScaleColumns(self, sr):
        """ScaleColumns(SparseMatrix self, Vector sr)"""
        return _sparsemat.SparseMatrix_ScaleColumns(self, sr)


    def __iadd__(self, B):
        """__iadd__(SparseMatrix self, SparseMatrix B) -> SparseMatrix"""
        val = _sparsemat.SparseMatrix___iadd__(self, B)

        val.thisown = 0
        return self


        return val


    def Add(self, *args):
        """
        Add(SparseMatrix self, int const i, int const j, double const a)
        Add(SparseMatrix self, double const a, SparseMatrix B)
        """
        return _sparsemat.SparseMatrix_Add(self, *args)


    def __imul__(self, a):
        """__imul__(SparseMatrix self, double a) -> SparseMatrix"""
        val = _sparsemat.SparseMatrix___imul__(self, a)

        val.thisown = 0
        return self


        return val


    def PrintMatlab(self, *args):
        """
        PrintMatlab(SparseMatrix self, std::ostream & out)
        PrintMatlab(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_PrintMatlab(self, *args)


    def PrintMM(self, *args):
        """
        PrintMM(SparseMatrix self, std::ostream & out)
        PrintMM(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_PrintMM(self, *args)


    def PrintCSR(self, out):
        """PrintCSR(SparseMatrix self, std::ostream & out)"""
        return _sparsemat.SparseMatrix_PrintCSR(self, out)


    def PrintCSR2(self, out):
        """PrintCSR2(SparseMatrix self, std::ostream & out)"""
        return _sparsemat.SparseMatrix_PrintCSR2(self, out)


    def PrintInfo(self, out):
        """PrintInfo(SparseMatrix self, std::ostream & out)"""
        return _sparsemat.SparseMatrix_PrintInfo(self, out)


    def IsSymmetric(self):
        """IsSymmetric(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_IsSymmetric(self)


    def Symmetrize(self):
        """Symmetrize(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_Symmetrize(self)


    def NumNonZeroElems(self):
        """NumNonZeroElems(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_NumNonZeroElems(self)


    def MaxNorm(self):
        """MaxNorm(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_MaxNorm(self)


    def CountSmallElems(self, tol):
        """CountSmallElems(SparseMatrix self, double tol) -> int"""
        return _sparsemat.SparseMatrix_CountSmallElems(self, tol)


    def CheckFinite(self):
        """CheckFinite(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_CheckFinite(self)


    def SetGraphOwner(self, ownij):
        """SetGraphOwner(SparseMatrix self, bool ownij)"""
        return _sparsemat.SparseMatrix_SetGraphOwner(self, ownij)


    def SetDataOwner(self, owna):
        """SetDataOwner(SparseMatrix self, bool owna)"""
        return _sparsemat.SparseMatrix_SetDataOwner(self, owna)


    def OwnsGraph(self):
        """OwnsGraph(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_OwnsGraph(self)


    def OwnsData(self):
        """OwnsData(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_OwnsData(self)


    def LoseData(self):
        """LoseData(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_LoseData(self)


    def Swap(self, other):
        """Swap(SparseMatrix self, SparseMatrix other)"""
        return _sparsemat.SparseMatrix_Swap(self, other)

    __swig_destroy__ = _sparsemat.delete_SparseMatrix
    __del__ = lambda self: None

    def GetType(self):
        """GetType(SparseMatrix self) -> mfem::Operator::Type"""
        return _sparsemat.SparseMatrix_GetType(self)


    def GetIArray(self):
        """GetIArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetIArray(self)


    def GetJArray(self):
        """GetJArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetJArray(self)


    def GetDataArray(self):
        """GetDataArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetDataArray(self)


    def Print(self, *args):
        """
        Print(SparseMatrix self, std::ostream & out, int width_=4)
        Print(SparseMatrix self, std::ostream & out)
        Print(SparseMatrix self)
        Print(SparseMatrix self, char const * file)
        """
        return _sparsemat.SparseMatrix_Print(self, *args)

SparseMatrix_swigregister = _sparsemat.SparseMatrix_swigregister
SparseMatrix_swigregister(SparseMatrix)


def SparseMatrixFunction(S, f):
    """SparseMatrixFunction(SparseMatrix S, double (*)(double) f)"""
    return _sparsemat.SparseMatrixFunction(S, f)

def TransposeAbstractSparseMatrix(A, useActualWidth):
    """TransposeAbstractSparseMatrix(AbstractSparseMatrix A, int useActualWidth) -> SparseMatrix"""
    return _sparsemat.TransposeAbstractSparseMatrix(A, useActualWidth)

def MultAbstractSparseMatrix(A, B):
    """MultAbstractSparseMatrix(AbstractSparseMatrix A, AbstractSparseMatrix B) -> SparseMatrix"""
    return _sparsemat.MultAbstractSparseMatrix(A, B)

def Mult_AtDA(A, D, OAtDA=None):
    """
    Mult_AtDA(SparseMatrix A, Vector D, SparseMatrix OAtDA=None) -> SparseMatrix
    Mult_AtDA(SparseMatrix A, Vector D) -> SparseMatrix
    """
    return _sparsemat.Mult_AtDA(A, D, OAtDA)
# This file is compatible with both classic and new-style classes.


