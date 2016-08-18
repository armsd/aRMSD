"""
Script to cythonize the core modules of aRMSD
"""

# Authors: Arne Wagner
# License: MIT

try:
    from setuptools import setup
    from setuptools import Extension

except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

from Cython.Build import cythonize

setup(name = 'acore', ext_modules = cythonize('acore.py'),)

setup(name = 'aplot', ext_modules = cythonize('aplot.py'),)

setup(name = 'alog', ext_modules = cythonize('alog.py'),)
