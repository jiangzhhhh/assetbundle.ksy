from assetbundle import Assetbundle


def extract(filename):
    bundle = Assetbundle.from_file(filename)
    blocks_info = bundle.archive_storage_header.blocks_info
    print "blocks", blocks_info.blocks_size

    archive_storage_body = "".join(block.uncompressed_data for block in bundle.archive_storage_body.blocks)
    print "archive_storage_body", len(bundle.archive_storage_body.blocks), len(archive_storage_body)

    print "directory_infos", len(blocks_info.directory_infos)
    for directory_info in blocks_info.directory_infos:
        data = archive_storage_body[directory_info.offset:directory_info.offset + directory_info.size]
        print directory_info.path, directory_info.size
        with open(directory_info.path, "wb") as f:
            f.write(data)
