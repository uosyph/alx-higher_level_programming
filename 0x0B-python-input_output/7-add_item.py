#!/usr/bin/python3
"""Adds all arguments to a list, then save them to a file"""

import sys

savefile = __import__('5-save_to_json_file').save_to_json_file
loadfile = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]

try:
    args_list = loadfile("add_item.json")
except Exception:
    args_list = []

args_list += args
savefile(args_list, "add_item.json")
