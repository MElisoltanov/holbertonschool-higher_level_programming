#!/usr/bin/python3
"""This module defines SwimMixin, FlyMixin, and Dragon classes for mixin demonstration."""

class SwimMixin:
    """Mixin providing swim ability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin providing fly ability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swim, fly, and roar abilities."""
    def roar(self):
        print("The dragon roars!")
