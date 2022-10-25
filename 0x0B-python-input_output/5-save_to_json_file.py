#!/usr/bin/python3
'''Module that writes an Object to a text file using a JSON rep'''
import json


def save_to_json_file(my_obj, filename):
    ''' Fn writes an Object to a text file using a JSON rep'''
    with open(filename, "w", encoding="UTF8") as myFile:
        json.load(my_obj, myFile)
