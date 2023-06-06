#!/usr/bin/python3
"""
Locked class module that prevents the user
from dynamically creating new instance attributes,
except if the new instance attribute is called.
"""


class LockedClass:
    """Locking __slots__
    """
    __slots__ = ['first_name']
