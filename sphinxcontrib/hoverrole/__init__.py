"""Sphinx hoverrole extension"""
from . import utils, dictlookup, createDicts

__version__ = "2.0.10"

def setup(app):
    LOG.info('initializing sphinxcontrib.hoverrole')
    return {
        'version': version.__version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
