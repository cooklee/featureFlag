import imp
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
all_flags = []
module_dir = 'flags'
for file in __all__:
    module = imp.load_source('module.name', '{}/{}.py'.format(module_dir, file))
    all_flags.append(module.flag)
