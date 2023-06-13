#!/usr/bin/python3
"""Adds all arguments to a list, then save them to a file"""

import sys
import os

savefile = __import__('5-save_to_json_file').save_to_json_file
loadfile = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args_list = []

if os.path.exists(filename):
    args_list = loadfile(filename)

for argum in sys.argv[1:]:
    args_list.append(argum)

savefile(args_list, filename)
