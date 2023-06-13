#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""

from sys import stdin

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(stdin):
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        if (i+1) % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
