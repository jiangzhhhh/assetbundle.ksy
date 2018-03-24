import lz4


class Decoder(object):
    def __init__(self, size):
        self.size = size

    def decode(self, buf):
        return lz4.block.decompress(buf, self.size)


def Lz4process(size):
    return Decoder(size)
