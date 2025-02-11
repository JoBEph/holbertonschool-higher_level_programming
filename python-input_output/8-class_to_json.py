#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON"""
import json


def class_to_json(obj):

    return obj.__dict__
