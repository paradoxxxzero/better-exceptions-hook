#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
better-exceptions import hook
"""
import sys
import os
from setuptools import setup
from distutils.sysconfig import get_python_lib

site_packages_path = get_python_lib().replace(sys.prefix + os.path.sep, '')

__version__ = "1.0.0"

setup(
    name="better-exceptions-hook",
    version=__version__,
    description="Import hook for better-exceptions",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    url="https://github.com/paradoxxxzero/better-exceptions-hook",
    license="MIT",
    platforms="Any",
    packages=['better_exceptions_hook'],
    data_files=[(site_packages_path, ['better_exceptions_hook.pth'])],
    install_requires=['better_exceptions'])
