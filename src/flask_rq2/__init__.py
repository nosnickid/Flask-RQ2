# -*- coding: utf-8 -*-
"""
    flask_rq2
    ~~~~~~~~~

    A Flask extension for RQ (Redis Queue).

    :copyright: (c) 2016 by Jannis Leidel.
    :license: MIT, see LICENSE for more details.
"""
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    try:
        from importlib_metadata import version, PackageNotFoundError
    except ImportError:
        version = None

from .app import RQ  # noqa

__author__ = 'Jannis Leidel'

__version__ = None
if version is not None:
    try:
        __version__ = version(__name__)
    except PackageNotFoundError:
        # package is not installed
        pass
