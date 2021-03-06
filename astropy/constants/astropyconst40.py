# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Astronomical and physics constants for Astropy v4.0.
See :mod:`astropy.constants` for a complete listing of constants defined
in Astropy.
"""
from astropy.utils import find_current_module
from . import utils as _utils
from . import codata2018, iau2015

codata = codata2018
iaudata = iau2015

_utils._set_c(codata, iaudata, find_current_module())

# Clean up namespace
del find_current_module
del _utils
