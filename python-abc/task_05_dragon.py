#!/usr/bin/env python3
"""explore mastery mixins"""


class SwimMixin:
    """Define Swim Mixin class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Define Fly Mixin class"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Define Dragon class with SwimMixin and FlyMixin"""

    def roar(self):
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
