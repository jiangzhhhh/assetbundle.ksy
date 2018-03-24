# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
from lz4process import Lz4process


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Assetbundle(KaitaiStruct):

    class CompressionMethod(Enum):
        lzma = 1
        lz4 = 2
        lz4hc = 3
        lzham = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.archive_storage_header = self._root.ArchiveStorageHeader(self._io, self, self._root)
        self.archive_storage_body = self._root.ArchiveStorageBody(self._io, self, self._root)

    class ArchiveStorageHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = self._root.ArchiveStorageHeader.Header(self._io, self, self._root)
            self._raw__raw_blocks_info = self._io.read_bytes(self.header.compressed_size)
            _process = Lz4process(self.header.uncompressed_size)
            self._raw_blocks_info = _process.decode(self._raw__raw_blocks_info)
            io = KaitaiStream(BytesIO(self._raw_blocks_info))
            self.blocks_info = self._root.ArchiveStorageHeader.BlocksInfo(io, self, self._root)

        class Header(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.signature = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.format = self._io.read_u4be()
                self.unity_major_version = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.unity_minor_version = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.file_size = self._io.read_s8be()
                self.compressed_size = self._io.read_u4be()
                self.uncompressed_size = self._io.read_u4be()
                self.flags = self._io.read_u4be()


        class BlocksInfo(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.guid = self._io.read_bytes(16)
                self.blocks_size = self._io.read_s4be()
                self.blocks = [None] * (self.blocks_size)
                for i in range(self.blocks_size):
                    self.blocks[i] = self._root.ArchiveStorageHeader.StorageBlock(self._io, self, self._root)

                self.directory_info_size = self._io.read_u4be()
                self.directory_infos = [None] * (self.directory_info_size)
                for i in range(self.directory_info_size):
                    self.directory_infos[i] = self._root.ArchiveStorageHeader.DirectoryInfo(self._io, self, self._root)



        class StorageBlock(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.uncompressed_size = self._io.read_u4be()
                self.compressed_size = self._io.read_u4be()
                self.flags = self._io.read_u2be()


        class DirectoryInfo(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.offset = self._io.read_u8be()
                self.size = self._io.read_u8be()
                self.flags = self._io.read_u4be()
                self.path = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")



    class ArchiveStorageBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.blocks = [None] * (self._parent.archive_storage_header.blocks_info.blocks_size)
            for i in range(self._parent.archive_storage_header.blocks_info.blocks_size):
                self.blocks[i] = self._root.ArchiveStorageBody.CompressedBlock(i, self._io, self, self._root)


        class CompressedBlock(KaitaiStruct):
            def __init__(self, i, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self.i = i
                self._read()

            def _read(self):
                self._raw_uncompressed_data = self._io.read_bytes(self._parent._parent.archive_storage_header.blocks_info.blocks[self.i].compressed_size)
                _process = Lz4process(self._parent._parent.archive_storage_header.blocks_info.blocks[self.i].uncompressed_size)
                self.uncompressed_data = _process.decode(self._raw_uncompressed_data)




