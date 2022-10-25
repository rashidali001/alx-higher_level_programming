#!/usr/bin/python3
'''adds all arguments to a Python list, and then save them to a file'''


import sys

save_to_json_file = __import__('5-save_tojson_file.py').save_to_json_file
load_from_json_file =\
    __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try:
    mylist = load_from_json_file(filename)
except Exception as e:
    mylist = []

for arg in sys.argv[1:]:
    mylist.append(arg)

save_to_json_file(mylist, filename)
