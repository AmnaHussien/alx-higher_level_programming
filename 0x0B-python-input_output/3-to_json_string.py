#!/usr/bin/python3
"""
function to convert into json
"""

import json


def to_json_string(my_obj):
    """  function that returns the JSON representation of an object """
    data = json.dumps(my_obj)
    return(data)
