#!/usr/bin/python3
'''Module that returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    ''' Function returning object(string)'''
    return json.dump(my_obj)
