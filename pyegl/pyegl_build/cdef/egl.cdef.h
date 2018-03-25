typedef void* EGLDisplay;
typedef void* EGLNativeDisplayType;
typedef unsigned int EGLBoolean;
typedef int32_t khronos_int32_t;
typedef khronos_int32_t EGLint;
typedef void* EGLSurface;


EGLDisplay eglGetDisplay(EGLNativeDisplayType display_id);
EGLBoolean eglInitialize(EGLDisplay dpy, EGLint *major, EGLint *minor);
