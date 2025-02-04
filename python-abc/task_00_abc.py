#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
Create an abstract class Animal with an abstract method sound.
"""


class Animal(ABC):
    """class animal from abc"""

    @abstractmethod
    def sound(self):
        """def sound"""
        pass


class Dog(Animal):
    """class dog from animal"""
    def sound(self):
        """sound from dog"""

        return "Bark"


class Cat(Animal):
    """cat animal class"""
    def sound(self):
        """sound from cat"""
        return "Meow"
