#!/usr/bin/python3
"""Adds all arguments to a list, then save them to a file"""

import sys

savefile = __import__('5-save_to_json_file').save_to_json_file
loadfile = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args_list = []

args_list = loadfile(filename)

for i in range(1, len(sys.argv)):
    args_list.append(sys.argv[i])

savefile(args_list, filename)
