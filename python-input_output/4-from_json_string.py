#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str : a JSON string.
    Return:
        an object (Python data structure).
    """
    return json.loads(my_str)
