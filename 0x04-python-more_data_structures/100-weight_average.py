#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_a = sum_b = weight = average = 0
    for i in my_list:
        sum_a += i[1]
        weight = i[0] * i[1]
        sum_b += weight
        average = sum_b / sum_a
    return average
