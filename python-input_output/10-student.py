#!/usr/bin/python3
"""import Student"""

Student = __import__('9-student').Student


class Student(Student):
    """ call student"""
    def to_json(self, attrs=None):
        """call def to json"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
