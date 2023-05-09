#!/usr/bin/python
for i in range(10):
    for j in range(i+1, 10):
        print("{0}{1}, ".format(i, j) if i == 0 and j == 1
              else "{0}{1}, ".format(i, j), end="")
