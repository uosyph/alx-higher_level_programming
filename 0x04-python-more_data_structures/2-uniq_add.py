#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    repetition = []
    for i in my_list:
        if i not in repetition:
            repetition.append(i)
            result += i
    return result
