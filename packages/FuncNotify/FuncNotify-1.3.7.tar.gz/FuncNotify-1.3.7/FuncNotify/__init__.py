"""
.. include:: ../README.md 
""" # For pdoc3

from os.path import dirname, basename, isfile, join
import glob
import importlib

module_list = glob.glob(join(dirname(__file__), "*Method.py"))
MODULES = [basename(f)[:-3] for f in module_list if isfile(f)]

def _import_all(modules: list):
    """Dynamic import of a module, similar to `from package import *` but specifically for this package

    Args:
        modules (list[str]): A file name in `FuncNotify` directory/package
    """    
    for mod in modules:
        try:
            module = importlib.import_module(f'FuncNotify.{mod}') 
            globals().update({k: v for (k, v) in module.__dict__.items() if not k.startswith('_')})
        except Exception as ex:
            print(f"Unable to import {mod} due to the following error\n " \
                  f"[ERROR] Exception: {ex}")

_import_all(MODULES)

from FuncNotify.NotifyDecorators import *
from FuncNotify.NotifyMethods import *
NotifyTypes=NotifyMethods.get_cls_registry()


import pkg_resources  # part of setuptools
__version__ = pkg_resources.require("FuncNotify")[0].version

__pdoc__={'FuncNotify.__main__': True}
"""Used only for pdoc documentation to inclue main for CLI documentation"""