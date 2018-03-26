typedef void* EGLDisplay;
typedef void* EGLNativeDisplayType;
typedef unsigned int EGLBoolean;
typedef int32_t khronos_int32_t;
typedef khronos_int32_t EGLint;
typedef void* EGLSurface;
typedef void* EGLConfig;
typedef void *EGLContext;
typedef void *EGLSync;
typedef void *EGLImage;


EGLDisplay eglGetDisplay(EGLNativeDisplayType display_id);
EGLBoolean eglInitialize(EGLDisplay display, EGLint *major, EGLint *minor);
EGLBoolean eglGetConfigs(EGLDisplay display, EGLConfig *configs, EGLint config_size, EGLint *num_config);
EGLBoolean eglChooseConfig (EGLDisplay dpy, const EGLint *attrib_list, EGLConfig *configs, EGLint config_size, EGLint *num_config);
