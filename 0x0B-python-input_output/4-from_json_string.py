#!/usr/bin/python3
'''Module returns an object Python data structure rep by a JSON string'''
import json


def from_json_string(my_str):
    '''Function returns python data structue'''
    return json.loads(my_str)
