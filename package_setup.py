#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setting up the current package for use
before using the package, You need to run this module so that
It can configure the whole package for your running env
"""
import os
import sys
from my_python.system.env_setup import append_path
from my_python.common.general import get_project_root_from_path


# check if the current file is a proper project or not
package_directory = get_project_root_from_path(__file__).root_path
if not package_directory:
    sys.exit(0)

# setup the PYTHON and BIN path for process
PYTHON_ROOT = os.path.join(package_directory, "src", os.path.basename(package_directory))
BIN_ROOT = os.path.join(package_directory, "src/bin")


# add the path to the system env
append_path(variable="PYTHONPATH", path=PYTHON_ROOT)
append_path(variable="PATH", path=BIN_ROOT)


# Now check if user has given any other arguments for installation and all
if sys.argv:
    if "install" in sys.argv:
        # we need to install the package on user host
        _py, process, live, override = sys.argv
        from scm_tools.common import scm_install_package, scm_install_bin_files
        scm_install_package(PYTHON_ROOT, for_qc=eval(live), override=eval(override))
        scm_install_bin_files(bin_directory=BIN_ROOT, for_qc=eval(live), override=eval(override))
