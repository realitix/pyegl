from cffi import FFI
from os import path


HERE = path.dirname(path.realpath(__file__))
INCLUDE_FOLDER = path.join(HERE, 'include')

# ----------
# BUILD WRAPPER
# ----------
ffibuilder = FFI()

# prepare cdef
cdef = open(path.join(HERE, 'cdef', 'egl.cdef.h')).read()
ffibuilder.cdef(cdef)

# prepare source
source = '''
#include <EGL/egl.h>
#include <EGL/eglext.h>
'''

ffibuilder.set_source(
    '_pyegl',
    source,
    libraries=['EGL'],
    extra_compile_args=["-I"+INCLUDE_FOLDER]
)


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
