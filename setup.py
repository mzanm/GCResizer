# GCResizer Build script.
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.

import shutil

shutil.rmtree("dist", True)
import sys
from distutils.core import setup


import py2exe

sys.argv.append("py2exe")

setup(
    py_modules=[],
    windows=["GCResizer.py"],
    zipfile=None,
    options={
        "py2exe": {
            "bundle_files": 2,
            "includes": ["imp"],
            "compressed": False,
            "excludes": [
                "_ssl",
                "http",
                "html",
                "pyreadline",
                "difflib",
                "tcl",
                "asyncio",
                "urllib",
                "socket",
                "_socket",
                "ssl",
                "wx.html",
                "wx.html2",
                "numpy",
                "setuptools",
                "distutils",
                "optparse",
                "pickle",
                "calendar",
                "pdb",
                "unittest",
                "test",
                "doctest",
                "tkinter",
                "email",
            ],
            "optimize": 2,
        }
    },
)
