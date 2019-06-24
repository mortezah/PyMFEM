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
        mname = '.'.join((pkg, '_communication')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_communication')
    _communication = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_communication', [dirname(__file__)])
        except ImportError:
            import _communication
            return _communication
        try:
            _mod = imp.load_module('_communication', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _communication = swig_import_helper()
    del swig_import_helper
else:
    import _communication
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

MFEM_VERSION = _communication.MFEM_VERSION
MFEM_VERSION_STRING = _communication.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _communication.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _communication.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _communication.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _communication.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _communication.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _communication.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _communication.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _communication.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _communication.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _communication.MFEM_HYPRE_VERSION
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.table
import mfem._par.sets
import mfem._par.ostream_typemap
class MPI_Session(_object):
    """Proxy of C++ mfem::MPI_Session class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MPI_Session, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MPI_Session, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::MPI_Session self) -> MPI_Session
        __init__(mfem::MPI_Session self, int & argc, char **& argv) -> MPI_Session
        """
        this = _communication.new_MPI_Session(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _communication.delete_MPI_Session
    __del__ = lambda self: None

    def WorldRank(self):
        """WorldRank(MPI_Session self) -> int"""
        return _communication.MPI_Session_WorldRank(self)


    def WorldSize(self):
        """WorldSize(MPI_Session self) -> int"""
        return _communication.MPI_Session_WorldSize(self)


    def Root(self):
        """Root(MPI_Session self) -> bool"""
        return _communication.MPI_Session_Root(self)

MPI_Session_swigregister = _communication.MPI_Session_swigregister
MPI_Session_swigregister(MPI_Session)

class GroupTopology(_object):
    """Proxy of C++ mfem::GroupTopology class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GroupTopology, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GroupTopology, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::GroupTopology self) -> GroupTopology
        __init__(mfem::GroupTopology self, MPI_Comm comm) -> GroupTopology
        __init__(mfem::GroupTopology self, GroupTopology gt) -> GroupTopology
        """
        this = _communication.new_GroupTopology(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetComm(self, comm):
        """SetComm(GroupTopology self, MPI_Comm comm)"""
        return _communication.GroupTopology_SetComm(self, comm)


    def GetComm(self):
        """GetComm(GroupTopology self) -> MPI_Comm"""
        return _communication.GroupTopology_GetComm(self)


    def MyRank(self):
        """MyRank(GroupTopology self) -> int"""
        return _communication.GroupTopology_MyRank(self)


    def NRanks(self):
        """NRanks(GroupTopology self) -> int"""
        return _communication.GroupTopology_NRanks(self)


    def Create(self, groups, mpitag):
        """Create(GroupTopology self, ListOfIntegerSets groups, int mpitag)"""
        return _communication.GroupTopology_Create(self, groups, mpitag)


    def NGroups(self):
        """NGroups(GroupTopology self) -> int"""
        return _communication.GroupTopology_NGroups(self)


    def GetNumNeighbors(self):
        """GetNumNeighbors(GroupTopology self) -> int"""
        return _communication.GroupTopology_GetNumNeighbors(self)


    def GetNeighborRank(self, i):
        """GetNeighborRank(GroupTopology self, int i) -> int"""
        return _communication.GroupTopology_GetNeighborRank(self, i)


    def IAmMaster(self, g):
        """IAmMaster(GroupTopology self, int g) -> bool"""
        return _communication.GroupTopology_IAmMaster(self, g)


    def GetGroupMaster(self, g):
        """GetGroupMaster(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMaster(self, g)


    def GetGroupMasterRank(self, g):
        """GetGroupMasterRank(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMasterRank(self, g)


    def GetGroupMasterGroup(self, g):
        """GetGroupMasterGroup(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupMasterGroup(self, g)


    def GetGroupSize(self, g):
        """GetGroupSize(GroupTopology self, int g) -> int"""
        return _communication.GroupTopology_GetGroupSize(self, g)


    def GetGroup(self, g):
        """GetGroup(GroupTopology self, int g) -> int const *"""
        return _communication.GroupTopology_GetGroup(self, g)


    def Load(self, arg2):
        """Load(GroupTopology self, std::istream & arg2)"""
        return _communication.GroupTopology_Load(self, arg2)


    def Copy(self, copy):
        """Copy(GroupTopology self, GroupTopology copy)"""
        return _communication.GroupTopology_Copy(self, copy)

    __swig_destroy__ = _communication.delete_GroupTopology
    __del__ = lambda self: None

    def Save(self, *args):
        """
        Save(GroupTopology self, std::ostream & out)
        Save(GroupTopology self, char const * file, int precision=8)
        Save(GroupTopology self, char const * file)
        """
        return _communication.GroupTopology_Save(self, *args)

GroupTopology_swigregister = _communication.GroupTopology_swigregister
GroupTopology_swigregister(GroupTopology)

class GroupCommunicator(_object):
    """Proxy of C++ mfem::GroupCommunicator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GroupCommunicator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GroupCommunicator, name)
    __repr__ = _swig_repr
    byGroup = _communication.GroupCommunicator_byGroup
    byNeighbor = _communication.GroupCommunicator_byNeighbor

    def __init__(self, *args):
        """
        __init__(mfem::GroupCommunicator self, GroupTopology gt, mfem::GroupCommunicator::Mode m) -> GroupCommunicator
        __init__(mfem::GroupCommunicator self, GroupTopology gt) -> GroupCommunicator
        """
        this = _communication.new_GroupCommunicator(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Create(self, ldof_group):
        """Create(GroupCommunicator self, intArray ldof_group)"""
        return _communication.GroupCommunicator_Create(self, ldof_group)


    def GroupLDofTable(self, *args):
        """
        GroupLDofTable(GroupCommunicator self) -> Table
        GroupLDofTable(GroupCommunicator self) -> Table
        """
        return _communication.GroupCommunicator_GroupLDofTable(self, *args)


    def Finalize(self):
        """Finalize(GroupCommunicator self)"""
        return _communication.GroupCommunicator_Finalize(self)


    def SetLTDofTable(self, ldof_ltdof):
        """SetLTDofTable(GroupCommunicator self, intArray ldof_ltdof)"""
        return _communication.GroupCommunicator_SetLTDofTable(self, ldof_ltdof)


    def GetGroupTopology(self, *args):
        """
        GetGroupTopology(GroupCommunicator self) -> GroupTopology
        GetGroupTopology(GroupCommunicator self) -> GroupTopology
        """
        return _communication.GroupCommunicator_GetGroupTopology(self, *args)

    __swig_destroy__ = _communication.delete_GroupCommunicator
    __del__ = lambda self: None

    def PrintInfo(self, *args):
        """
        PrintInfo(GroupCommunicator self, std::ostream & out)
        PrintInfo(GroupCommunicator self)
        PrintInfo(GroupCommunicator self, char const * file, int precision=8)
        PrintInfo(GroupCommunicator self, char const * file)
        """
        return _communication.GroupCommunicator_PrintInfo(self, *args)

GroupCommunicator_swigregister = _communication.GroupCommunicator_swigregister
GroupCommunicator_swigregister(GroupCommunicator)


def ReorderRanksZCurve(comm):
    """ReorderRanksZCurve(MPI_Comm comm) -> MPI_Comm"""
    return _communication.ReorderRanksZCurve(comm)
# This file is compatible with both classic and new-style classes.


