#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
Create an abstract class Animal with an abstract method sound.
"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "bark"


class Cat(Animal):
    def sound(self):
        return "meow"
