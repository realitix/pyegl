from pyegl._pyegl import ffi, lib


EGL_DEFAULT_DISPLAY = ffi.cast('EGLNativeDisplayType', 0)
EGL_NO_DISPLAY = ffi.cast('EGLDisplay', 0)


def eglGetDisplay(display_id):
    return lib.eglGetDisplay(display_id)
