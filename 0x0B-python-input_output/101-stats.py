#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

from sys import stdin


def print_stats(size, status_codes):
    """Prints final metrics"""
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


# Initialize variables to keep track of metrics
size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
counter = 0

try:
    # Read input line by line
    for line in stdin:
        # Update metrics
        if counter == 10:
            # Print metrics every 10 lines
            print_stats(size, status_codes)
            counter = 1
        else:
            counter += 1

        # Parse the line to extract file size
        line = line.split()
        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        # Parse the line to extract status code
        try:
            if line[-2] in valid_codes:
                if status_codes.get(line[-2], -1) == -1:
                    status_codes[line[-2]] = 1
                else:
                    status_codes[line[-2]] += 1
        except IndexError:
            pass

    # Print final metrics
    print_stats(size, status_codes)

except KeyboardInterrupt:
    # Print final metrics on keyboard interrupt
    print_stats(size, status_codes)
    raise
