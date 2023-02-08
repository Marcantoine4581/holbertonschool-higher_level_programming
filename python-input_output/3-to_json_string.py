#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj : The oject.
    Return:
        the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
