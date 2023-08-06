import os

def _bootstrap():
    global _bootstrap, __loader__, __file__
    import sys, pkg_resources, imp
    shared_object_file = 'pycompadre.cpython-36m-x86_64-linux-gnu.so'
    try:
        __file__ = pkg_resources.resource_filename(__name__, os.path.basename(shared_object_file))
        __loader__ = None
        del _bootstrap, __loader__
        imp.load_dynamic(__name__, __file__)
    except:
        print("Failed to load: " + shared_object_file)
_bootstrap()
