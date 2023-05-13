#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    length = 0
    for i in range(len(my_list)):
        if length < my_list[i]:
            length = my_list[i]
    return length
