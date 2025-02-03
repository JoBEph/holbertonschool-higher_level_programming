#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    
    def dog(self):
        self.sound("bark")
    def cat(self):
        self.sound("meow")
