from cffi import FFI
from os import path
import platform


HERE = path.dirname(path.realpath(__file__))
INCLUDE_FOLDER = path.join(HERE, 'include')
LINUX = platform.system() == 'Linux'

# ----------
# BUILD WRAPPER
# ----------
ffibuilder = FFI()

# prepare cdef
cdef = ""
#if LINUX:
#    cdef += open(path.join(HERE, 'cdef', 'stddef.cdef.h')).read()
cdef += open(path.join(HERE, 'cdef', 'egl.cdef.h')).read()

ffibuilder.cdef(cdef)


# prepare libraries
libs = ['vk_mem_alloc']

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
