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
        mname = '.'.join((pkg, '_pncmesh')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pncmesh')
    _pncmesh = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pncmesh', [dirname(__file__)])
        except ImportError:
            import _pncmesh
            return _pncmesh
        try:
            _mod = imp.load_module('_pncmesh', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pncmesh = swig_import_helper()
    del swig_import_helper
else:
    import _pncmesh
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


MFEM_VERSION = _pncmesh.MFEM_VERSION
MFEM_VERSION_STRING = _pncmesh.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pncmesh.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pncmesh.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pncmesh.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pncmesh.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pncmesh.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pncmesh.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _pncmesh.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _pncmesh.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _pncmesh.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _pncmesh.MFEM_HYPRE_VERSION
import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.handle
import mfem._par.hypre
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.communication
import mfem._par.sets
import mfem._par.ostream_typemap
class ParNCMesh(mfem._par.ncmesh.NCMesh):
    """Proxy of C++ mfem::ParNCMesh class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.ncmesh.NCMesh]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParNCMesh, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.ncmesh.NCMesh]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParNCMesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::ParNCMesh self, MPI_Comm comm, NCMesh ncmesh, int * part=None) -> ParNCMesh
        __init__(mfem::ParNCMesh self, MPI_Comm comm, NCMesh ncmesh) -> ParNCMesh
        __init__(mfem::ParNCMesh self, ParNCMesh other) -> ParNCMesh
        """
        this = _pncmesh.new_ParNCMesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pncmesh.delete_ParNCMesh
    __del__ = lambda self: None

    def Refine(self, refinements):
        """Refine(ParNCMesh self, mfem::Array< mfem::Refinement > const & refinements)"""
        return _pncmesh.ParNCMesh_Refine(self, refinements)


    def LimitNCLevel(self, max_nc_level):
        """LimitNCLevel(ParNCMesh self, int max_nc_level)"""
        return _pncmesh.ParNCMesh_LimitNCLevel(self, max_nc_level)


    def CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level):
        """CheckDerefinementNCLevel(ParNCMesh self, Table deref_table, intArray level_ok, int max_nc_level)"""
        return _pncmesh.ParNCMesh_CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level)


    def Derefine(self, derefs):
        """Derefine(ParNCMesh self, intArray derefs)"""
        return _pncmesh.ParNCMesh_Derefine(self, derefs)


    def Rebalance(self):
        """Rebalance(ParNCMesh self)"""
        return _pncmesh.ParNCMesh_Rebalance(self)


    def GetNElements(self):
        """GetNElements(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetNElements(self)


    def GetNGhostVertices(self):
        """GetNGhostVertices(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetNGhostVertices(self)


    def GetNGhostEdges(self):
        """GetNGhostEdges(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetNGhostEdges(self)


    def GetNGhostFaces(self):
        """GetNGhostFaces(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetNGhostFaces(self)


    def GetNGhostElements(self):
        """GetNGhostElements(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetNGhostElements(self)


    def GetGhostFaceGeometry(self, ghost_face_id):
        """GetGhostFaceGeometry(ParNCMesh self, int ghost_face_id) -> mfem::Geometry::Type"""
        return _pncmesh.ParNCMesh_GetGhostFaceGeometry(self, ghost_face_id)


    def GetSharedVertices(self):
        """GetSharedVertices(ParNCMesh self) -> mfem::NCMesh::NCList const &"""
        return _pncmesh.ParNCMesh_GetSharedVertices(self)


    def GetSharedEdges(self):
        """GetSharedEdges(ParNCMesh self) -> mfem::NCMesh::NCList const &"""
        return _pncmesh.ParNCMesh_GetSharedEdges(self)


    def GetSharedFaces(self):
        """GetSharedFaces(ParNCMesh self) -> mfem::NCMesh::NCList const &"""
        return _pncmesh.ParNCMesh_GetSharedFaces(self)


    def GetSharedList(self, entity):
        """GetSharedList(ParNCMesh self, int entity) -> mfem::NCMesh::NCList const &"""
        return _pncmesh.ParNCMesh_GetSharedList(self, entity)


    def GetFaceOrientation(self, index):
        """GetFaceOrientation(ParNCMesh self, int index) -> int"""
        return _pncmesh.ParNCMesh_GetFaceOrientation(self, index)


    def GetEntityOwnerId(self, entity, index):
        """GetEntityOwnerId(ParNCMesh self, int entity, int index) -> mfem::ParNCMesh::GroupId"""
        return _pncmesh.ParNCMesh_GetEntityOwnerId(self, entity, index)


    def GetEntityGroupId(self, entity, index):
        """GetEntityGroupId(ParNCMesh self, int entity, int index) -> mfem::ParNCMesh::GroupId"""
        return _pncmesh.ParNCMesh_GetEntityGroupId(self, entity, index)


    def GetGroup(self, id):
        """GetGroup(ParNCMesh self, mfem::ParNCMesh::GroupId id) -> mfem::ParNCMesh::CommGroup const &"""
        return _pncmesh.ParNCMesh_GetGroup(self, id)


    def GroupContains(self, id, rank):
        """GroupContains(ParNCMesh self, mfem::ParNCMesh::GroupId id, int rank) -> bool"""
        return _pncmesh.ParNCMesh_GroupContains(self, id, rank)


    def IsGhost(self, entity, index):
        """IsGhost(ParNCMesh self, int entity, int index) -> bool"""
        return _pncmesh.ParNCMesh_IsGhost(self, entity, index)


    def ElementRank(self, index):
        """ElementRank(ParNCMesh self, int index) -> int"""
        return _pncmesh.ParNCMesh_ElementRank(self, index)


    def GetMyRank(self):
        """GetMyRank(ParNCMesh self) -> int"""
        return _pncmesh.ParNCMesh_GetMyRank(self)


    def SendRebalanceDofs(self, old_ndofs, old_element_dofs, old_global_offset, space):
        """SendRebalanceDofs(ParNCMesh self, int old_ndofs, Table old_element_dofs, long old_global_offset, FiniteElementSpace space)"""
        return _pncmesh.ParNCMesh_SendRebalanceDofs(self, old_ndofs, old_element_dofs, old_global_offset, space)


    def RecvRebalanceDofs(self, elements, dofs):
        """RecvRebalanceDofs(ParNCMesh self, intArray elements, mfem::Array< long > & dofs)"""
        return _pncmesh.ParNCMesh_RecvRebalanceDofs(self, elements, dofs)


    def GetRebalanceOldIndex(self):
        """GetRebalanceOldIndex(ParNCMesh self) -> intArray"""
        return _pncmesh.ParNCMesh_GetRebalanceOldIndex(self)


    def GetDerefineOldRanks(self):
        """GetDerefineOldRanks(ParNCMesh self) -> intArray"""
        return _pncmesh.ParNCMesh_GetDerefineOldRanks(self)


    def GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges):
        """GetBoundaryClosure(ParNCMesh self, intArray bdr_attr_is_ess, intArray bdr_vertices, intArray bdr_edges)"""
        return _pncmesh.ParNCMesh_GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges)


    def Trim(self):
        """Trim(ParNCMesh self)"""
        return _pncmesh.ParNCMesh_Trim(self)


    def MemoryUsage(self, with_base=True):
        """
        MemoryUsage(ParNCMesh self, bool with_base=True) -> long
        MemoryUsage(ParNCMesh self) -> long
        """
        return _pncmesh.ParNCMesh_MemoryUsage(self, with_base)


    def PrintMemoryDetail(self, with_base=True):
        """
        PrintMemoryDetail(ParNCMesh self, bool with_base=True) -> int
        PrintMemoryDetail(ParNCMesh self) -> int
        """
        return _pncmesh.ParNCMesh_PrintMemoryDetail(self, with_base)


    def GetDebugMesh(self, debug_mesh):
        """GetDebugMesh(ParNCMesh self, Mesh debug_mesh)"""
        return _pncmesh.ParNCMesh_GetDebugMesh(self, debug_mesh)

ParNCMesh_swigregister = _pncmesh.ParNCMesh_swigregister
ParNCMesh_swigregister(ParNCMesh)


def __lt__(a, b):
    """__lt__(mfem::NCMesh::MeshId const & a, mfem::NCMesh::MeshId const & b) -> bool"""
    return _pncmesh.__lt__(a, b)

def __eq__(a, b):
    """__eq__(mfem::NCMesh::MeshId const & a, mfem::NCMesh::MeshId const & b) -> bool"""
    return _pncmesh.__eq__(a, b)
# This file is compatible with both classic and new-style classes.


