#!/usr/bin/python3
"""Adds all arguments to a list, then save them to a file"""

import sys
savefile = __import__('5-save_to_json_file').save_to_json_file
loadfile = __import__('6-load_from_json_file').load_from_json_file


try:
    lst = loadfile("add_item.json")
except:
    lst = []

for i in range(1, len(sys.argv)):
    lst.append(sys.argv[i])

savefile(lst, "add_item.json")
