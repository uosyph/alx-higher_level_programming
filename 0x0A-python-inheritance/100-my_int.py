#!/usr/bin/python3
"""MyInt class that inherits from int."""


class MyInt(int):
    """Custom int class where == and != operators inverted."""

    def __eq__(self, other):
        """Equality comparison"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Equality comparison"""
        return not super().__ne__(other)
