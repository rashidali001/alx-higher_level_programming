#!/usr/bin/python3
'''creates an Object from a “JSON file'''
import json


def load_from_json_file(filename):
    ''' Returns an Object from a “JSON file'''
    with open(filename, "r", encoding="UTF8") as filename:
        object_file = json.loads(filename.read())
    return object_file
