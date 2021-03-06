#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Package setup
"""
import os
from setuptools import setup, find_packages

PKG_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def get_long_description():
    description_files = [f for f in os.listdir(PKG_DIR_PATH) if "readme" in str(f).lower()]
    if not description_files:
        return " "

    with open(description_files[0], encoding="utf-8") as f:
        long_description = f.read()
      
    return long_description

  
def get_script_files():
    script_files = list()

    # executable scripts should be in these directories only
    keywords = ("bin", "script")

    for root, dirs, files in os.walk(PKG_DIR_PATH):
        if str(root).endswith(keywords):

            for exe_file in files:
                exe_path = os.path.join(root, exe_file)
                script_files.append(os.path.relpath(exe_path, PKG_DIR_PATH))

                # TODO: Add logic to check file permissions as well for exe files

    return script_files


setup(name              = os.path.basename(PKG_DIR_PATH),
      version           = "0.1.0",
      author            = 'Arjun Prasad Namdeo',
      author_email      = 'arjun.namdeo.vfx@gmail.com',
      license           = 'MIT',
      description       = "generic python package for my day to day usage",
      long_description  = get_long_description(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Human Machine Interfaces',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Logging',
          'Topic :: Terminals',
          ],
      keywords          = "python handy useful",
      packages          = find_packages(exclude=["tests", "contrib", "docs"]),
      install_requires  = ["coloredlogs"],
      include_package_data = True,
      dependency_links  = [],
      scripts           = get_script_files(),
      zip_safe          = False,
      url               = "https://github.com/arjun-namdeo/{}".format(os.path.basename(PKG_DIR_PATH)))
