from distutils.command.build import build
from setuptools import setup
from os import path
import platform


setup(
    name="pyegl",
    version="0.1",
    author="realitix",
    author_email="realitix@gmail.com",
    description="Python CFFI binding for EGL",
    long_description="Python CFFI binding for EGL",
    packages=['pyegl'],
    install_requires=["cffi"],
    setup_requires=["cffi"],
    include_package_data=True,
    url="http://github.com/realitix/pyegl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    license="Apache 2.0",
    ext_package="pyegl",
    cffi_modules=["pyegl/pyegl_build/pyegl_build.py:ffibuilder"]
)
