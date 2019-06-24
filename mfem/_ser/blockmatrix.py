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
        mname = '.'.join((pkg, '_blockmatrix')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_blockmatrix')
    _blockmatrix = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_blockmatrix', [dirname(__file__)])
        except ImportError:
            import _blockmatrix
            return _blockmatrix
        try:
            _mod = imp.load_module('_blockmatrix', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _blockmatrix = swig_import_helper()
    del swig_import_helper
else:
    import _blockmatrix
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
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.sparsemat
import mfem._ser.densemat
class BlockMatrix(mfem._ser.matrix.AbstractSparseMatrix):
    """Proxy of C++ mfem::BlockMatrix class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.AbstractSparseMatrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.AbstractSparseMatrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BlockMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::BlockMatrix self, intArray offsets) -> BlockMatrix
        __init__(mfem::BlockMatrix self, intArray row_offsets, intArray col_offsets) -> BlockMatrix
        """
        this = _blockmatrix.new_BlockMatrix(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        from mfem.ser import intArray  
        if len(args) == 1:
           if isinstance(args[0], intArray):
               self._offsets = args[0]
        if len(args) == 2:
           if (isinstance(args[0], intArray) and
               isinstance(args[1], intArray)):
               self._offsets = (args[0], args[1])




    def SetBlock(self, i, j, mat):
        """SetBlock(BlockMatrix self, int i, int j, SparseMatrix mat)"""
        val = _blockmatrix.BlockMatrix_SetBlock(self, i, j, mat)

        if not hasattr(self, '_linked_mat'):
           self._linked_mat = {}
        self._linked_mat[i, j] = mat


        return val


    def NumRowBlocks(self):
        """NumRowBlocks(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumRowBlocks(self)


    def NumColBlocks(self):
        """NumColBlocks(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumColBlocks(self)


    def GetBlock(self, *args):
        """
        GetBlock(BlockMatrix self, int i, int j) -> SparseMatrix
        GetBlock(BlockMatrix self, int i, int j) -> SparseMatrix
        """
        return _blockmatrix.BlockMatrix_GetBlock(self, *args)


    def IsZeroBlock(self, i, j):
        """IsZeroBlock(BlockMatrix self, int i, int j) -> int"""
        return _blockmatrix.BlockMatrix_IsZeroBlock(self, i, j)


    def RowOffsets(self, *args):
        """
        RowOffsets(BlockMatrix self) -> intArray
        RowOffsets(BlockMatrix self) -> intArray
        """
        return _blockmatrix.BlockMatrix_RowOffsets(self, *args)


    def ColOffsets(self, *args):
        """
        ColOffsets(BlockMatrix self) -> intArray
        ColOffsets(BlockMatrix self) -> intArray
        """
        return _blockmatrix.BlockMatrix_ColOffsets(self, *args)


    def RowSize(self, i):
        """RowSize(BlockMatrix self, int const i) -> int"""
        return _blockmatrix.BlockMatrix_RowSize(self, i)


    def EliminateRowCol(self, *args):
        """
        EliminateRowCol(BlockMatrix self, int rc, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateRowCol(BlockMatrix self, int rc)
        EliminateRowCol(BlockMatrix self, intArray ess_bc_dofs, Vector sol, Vector rhs)
        """
        return _blockmatrix.BlockMatrix_EliminateRowCol(self, *args)


    def Finalize(self, *args):
        """
        Finalize(BlockMatrix self, int skip_zeros=1)
        Finalize(BlockMatrix self)
        Finalize(BlockMatrix self, int skip_zeros, bool fix_empty_rows)
        """
        return _blockmatrix.BlockMatrix_Finalize(self, *args)


    def CreateMonolithic(self):
        """CreateMonolithic(BlockMatrix self) -> SparseMatrix"""
        return _blockmatrix.BlockMatrix_CreateMonolithic(self)


    def Elem(self, *args):
        """
        Elem(BlockMatrix self, int i, int j) -> double
        Elem(BlockMatrix self, int i, int j) -> double const &
        """
        return _blockmatrix.BlockMatrix_Elem(self, *args)


    def Inverse(self):
        """Inverse(BlockMatrix self) -> MatrixInverse"""
        return _blockmatrix.BlockMatrix_Inverse(self)


    def NumNonZeroElems(self):
        """NumNonZeroElems(BlockMatrix self) -> int"""
        return _blockmatrix.BlockMatrix_NumNonZeroElems(self)


    def GetRow(self, row, cols, srow):
        """GetRow(BlockMatrix self, int const row, intArray cols, Vector srow) -> int"""
        return _blockmatrix.BlockMatrix_GetRow(self, row, cols, srow)


    def EliminateZeroRows(self, threshold=1e-12):
        """
        EliminateZeroRows(BlockMatrix self, double const threshold=1e-12)
        EliminateZeroRows(BlockMatrix self)
        """
        return _blockmatrix.BlockMatrix_EliminateZeroRows(self, threshold)


    def Mult(self, x, y):
        """Mult(BlockMatrix self, Vector x, Vector y)"""
        return _blockmatrix.BlockMatrix_Mult(self, x, y)


    def AddMult(self, x, y, val=1.):
        """
        AddMult(BlockMatrix self, Vector x, Vector y, double const val=1.)
        AddMult(BlockMatrix self, Vector x, Vector y)
        """
        return _blockmatrix.BlockMatrix_AddMult(self, x, y, val)


    def MultTranspose(self, x, y):
        """MultTranspose(BlockMatrix self, Vector x, Vector y)"""
        return _blockmatrix.BlockMatrix_MultTranspose(self, x, y)


    def AddMultTranspose(self, x, y, val=1.):
        """
        AddMultTranspose(BlockMatrix self, Vector x, Vector y, double const val=1.)
        AddMultTranspose(BlockMatrix self, Vector x, Vector y)
        """
        return _blockmatrix.BlockMatrix_AddMultTranspose(self, x, y, val)

    __swig_destroy__ = _blockmatrix.delete_BlockMatrix
    __del__ = lambda self: None
    __swig_setmethods__["owns_blocks"] = _blockmatrix.BlockMatrix_owns_blocks_set
    __swig_getmethods__["owns_blocks"] = _blockmatrix.BlockMatrix_owns_blocks_get
    if _newclass:
        owns_blocks = _swig_property(_blockmatrix.BlockMatrix_owns_blocks_get, _blockmatrix.BlockMatrix_owns_blocks_set)

    def PrintMatlab(self, *args):
        """
        PrintMatlab(BlockMatrix self, std::ostream & os)
        PrintMatlab(BlockMatrix self)
        PrintMatlab(BlockMatrix self, char const * file, int precision=8)
        PrintMatlab(BlockMatrix self, char const * file)
        """
        return _blockmatrix.BlockMatrix_PrintMatlab(self, *args)

BlockMatrix_swigregister = _blockmatrix.BlockMatrix_swigregister
BlockMatrix_swigregister(BlockMatrix)

# This file is compatible with both classic and new-style classes.


