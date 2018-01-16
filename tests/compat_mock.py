# To simplify this test suite. Inspired by django/test/__init__.py
try:
    from unittest.mock import *  # NOQA
except ImportError:
    try:
        from mock import *  # NOQA
    except ImportError:
        pass
