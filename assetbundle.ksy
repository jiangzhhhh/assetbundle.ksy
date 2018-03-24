meta:
  id: assetbundle
  file-extension: assetbundle
  endian: be
  encoding: UTF-8
seq:
  - id: archive_storage_header
    type: archive_storage_header
  - id: archive_storage_body
    type: archive_storage_body
types:
  archive_storage_header:
    seq: 
      - id: header
        type: header
      - id: blocks_info
        type: blocks_info
        size: header.compressed_size
        process: lz4process(header.uncompressed_size)
    types:
      header:
        seq:
          - id: signature
            type: strz
          - id: format
            type: u4
          - id: unity_major_version
            type: strz
          - id: unity_minor_version
            type: strz
          - id: file_size
            type: s8
          - id: compressed_size
            type: u4
          - id: uncompressed_size
            type: u4
          - id: flags
            type: u4
      blocks_info:
        seq:
          - id: guid
            size: 16
          - id: blocks_size
            type: s4
          - id: blocks
            type: storage_block
            repeat: expr
            repeat-expr: blocks_size
          - id: directory_info_size
            type: u4
          - id: directory_infos
            type: directory_info
            repeat: expr
            repeat-expr: directory_info_size
      storage_block:
        seq:
          - id: uncompressed_size
            type: u4
          - id: compressed_size
            type: u4
          - id: flags
            type: u2
      directory_info:
        seq:
          - id: offset
            type: u8
          - id: size
            type: u8
          - id: flags
            type: u4
          - id: path
            type: strz
  archive_storage_body:
    seq:
      - id: blocks
        type: compressed_block(_index)
        repeat: expr
        repeat-expr: _parent.archive_storage_header.blocks_info.blocks_size
    types:
      compressed_block:
        params:
            - id: i
              type: u4
        seq:
          - id: uncompressed_data
            size: _parent._parent.archive_storage_header.blocks_info.blocks[i].compressed_size
            process: lz4process(_parent._parent.archive_storage_header.blocks_info.blocks[i].uncompressed_size)
enums:
  compression_method:
    1: lzma
    3: lz4
    2: lz4
    3: lz4hc
    4: lzham
