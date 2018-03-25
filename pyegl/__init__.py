from pyegl._pyegl import ffi, lib


EGL_DEFAULT_DISPLAY = ffi.cast('EGLNativeDisplayType', 0)
EGL_NO_DISPLAY = ffi.cast('EGLDisplay', 0)
EGL_NO_SURFACE = ffi.cast('EGLSurface', 0)


class EglError(Exception):
    pass


def eglGetDisplay(display_id):
    return lib.eglGetDisplay(display_id)


def eglInitialize(dpy):
    major = ffi.new('EGLint*')
    minor = ffi.new('EGLint*')
    result = lib.eglInitialize(dpy, major, minor)

    if not result:
        raise EglError("Can't initialize display")

    return major[0], minor[0]
