#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return new_list
    for i in new_list:
        if i == idx:
            new_list[i] = element
            return new_list
