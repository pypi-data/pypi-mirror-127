from struct import pack
import logging
log = logging.getLogger()


class VoxWriter(object):

    def __init__(self, filename, vox):
        self.filename = filename
        self.vox = vox

    def _chunk(self, id, content, chunks=[]):

        res = b''
        for c in chunks:
            res += self._chunk(*c)

        return pack('4sii', id, len(content), len(res)) + content + res

    def _matflags(self, props):
        flags = 0
        res = b''
        for b, field in [(0, 'plastic'),
                         (1, 'roughness'),
                         (2, 'specular'),
                         (3, 'IOR'),
                         (4, 'attenuation'),
                         (5, 'power'),
                         (6, 'glow'),
                         (7, 'isTotalPower')]:
            if field in props:
                flags |= 1 << b
                try:
                    res += pack('f', props[field])
                except Exception as exc:
                    print(f"Bad prop content: {props[field]} ({type(props[field])}) expected float.")
                    raise exc

        return pack('i', flags) + res

    def write(self):

        res = pack('4si', b'VOX ', 150)

        chunks = []

        if len(self.vox.models) > 1:
            chunks.append((b'PACK', pack('i', len(self.vox.models))))

        for m in self.vox.models:
            chunks.append((b'SIZE', pack('iii', *m.size)))
            new_voxels = [pack('BBBB', *v) for v in m.voxels]
            new_chunk = pack('i', len(m.voxels)) + b''.join(new_voxels)
            log.debug(f"New chunk: {new_chunk}")
            chunks.append((b'XYZI', new_chunk))

        chunks.append((b'RGBA', b''.join(pack('BBBB', *c) for c in self.vox.palette)))

        for m in self.vox.materials:
            if m:
                chunks.append((b'MATT', pack('iif', m.id, m.type, m.weight) + self._matflags(m.props)))

        # TODO materials

        res += self._chunk(b'MAIN', b'', chunks)

        with open(self.filename, 'wb') as f:
            f.write(res)
