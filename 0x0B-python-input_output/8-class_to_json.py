#!/usr/bin/python3
"""Contains the "class_to_json" function"""

def class_to_json(obj):
    """Returns the dictionary description with
    a simple data structure for JSON
    serialization of an object."""
    attributes = obj.__dict__.copy()
    for key, value in attributes.items():
        if hasattr(value, "__dict__"):
            attributes[key] = value.__dict__
    return attributes
