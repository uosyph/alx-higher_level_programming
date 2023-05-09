#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(''.join([chr(ord(char))]), end="")
