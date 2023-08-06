from struct import unpack_from as unpack, calcsize, unpack_from
import logging

from .models import Vox, Size, Voxel, Model, Material

log = logging.getLogger(__name__)

MATERIALS = [(0, 'plastic'),
     (1, 'roughness'),
     (2, 'specular'),
     (3, 'IOR'),
     (4, 'attenuation'),
     (5, 'power'),
     (6, 'glow'),
     (7, 'isTotalPower')]

class ParsingException(Exception):
    pass


def bit(val, offset):
    mask = 1 << offset
    return val & mask


class Chunk(object):
    def __init__(self, chunk_id, content=None, chunks=None):
        self.id = chunk_id
        self.content = content or b''
        self.chunks = chunks or []
        self.material = None

        if chunk_id == b'MAIN':
            if len(self.content):
                raise ParsingException('Non-empty content for main chunk')
        elif chunk_id == b'PACK':
            self.models = unpack('i', content)[0]
        elif chunk_id == b'SIZE':
            self.size = Size(*unpack('iii', content))
        elif chunk_id == b'XYZI':
            # verified. issue must come when packing.
            log.debug(f"XYZI bytes: {content}")
            n = unpack('i', content)[0]
            log.debug(f'xyzi block with {n} voxels (len {len(content)})')
            self.voxels = []
            self.voxels = [Voxel(*unpack('BBBB', content, offset=4 + 4 * i)) for i in range(n)]
            log.debug(self.voxels)
        elif chunk_id == b'RGBA':
            self.palette = [(unpack('BBBB', content, 4 * i)) for i in range(255)]
            # Docs say:  color [0-254] are mapped to palette index [1-255]
            # hmm
            # self.palette = [ Color(0,0,0,0) ] + [ Color(*unpack('BBBB', content, 4*i)) for i in range(255) ]
        elif chunk_id == b'MATT' or chunk_id == b'MATL':
            _id, _type, weight, flags = unpack('iifi', content)
            props = {}
            offset = 16
            for b, field in MATERIALS:
                if bit(flags, b) and b < 7:  # no value for 7 / isTotalPower
                    props[field] = unpack('f', content, offset)[0]
                    offset += 4

            self.material = Material(_id, _type, weight, props)

        else:
            # raise ParsingException('Unknown chunk type: %s'%self.id)
            log.debug(f"Unknown chunk type {chunk_id}")
            pass

    def __str__(self):
        s = f"Chunk with id {self.id}"
        return s


class VoxParser(object):

    def __init__(self, filename):
        with open(filename, 'rb') as f:
            self.content = f.read()

        self.offset = 0

    def unpack(self, fmt):
        r = unpack(fmt, self.content, self.offset)
        self.offset += calcsize(fmt)
        return r

    def _parse_chunk(self):

        _id, n, m = self.unpack('4sii')

        log.debug("Found chunk id %s / len %s / children %s", _id, n, m)

        content = self.unpack('%ds' % n)[0]

        start = self.offset
        chunks = []
        while self.offset < start + m:
            chunks.append(self._parse_chunk())

        return Chunk(_id, content, chunks)

    def parse(self):

        header, version = self.unpack('4si')

        if header != b'VOX ':
            raise ParsingException("This doesn't look like a vox file to me")

        if version != 150:
            raise ParsingException("Unknown vox version: %s expected 150" % version)

        main = self._parse_chunk()

        if main.id != b'MAIN':
            raise ParsingException("Missing MAIN Chunk")

        chunks = list(reversed(main.chunks))
        if chunks[-1].id == b'PACK':
            models = chunks.pop().models
        else:
            models = 1

        log.debug("file has %d models", models)

        models = [self._parse_model(size=chunks.pop(), xyzi=chunks.pop()) for _ in range(models)]

        palette = None
        materials = []
        for chunk in chunks:
            if chunk.id == b'RGBA':
                log.debug("Parsed RGBA chunk")
                palette = chunk.palette
            elif chunk.id == b'MATT' or chunk.id == b'MATL':
                log.debug(f"Parsed {chunk.id} chunk")
                materials.append(chunk.material)
            else:
                log.debug(f"Skipping Chunk with id {chunk.id}")

        return Vox(models, palette, materials).to_dense(), palette

    def _parse_model(self, size, xyzi):
        if size.id != b'SIZE':
            raise ParsingException('Expected SIZE chunk, got %s', size.id)
        if xyzi.id != b'XYZI':
            raise ParsingException('Expected XYZI chunk, got %s', xyzi.id)

        return Model(size.size, xyzi.voxels)


if __name__ == '__main__':
    import sys
    import coloredlogs

    coloredlogs.install(level=logging.DEBUG)

    VoxParser(sys.argv[1]).parse()
