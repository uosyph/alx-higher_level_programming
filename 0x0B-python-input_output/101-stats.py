#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


import sys

TOTAL_FILE_SIZE = 0
STATUS_CODES = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
LINES_PROCESSED = 0

try:
    for line in sys.stdin:
        try:
            ip_address, _, _, timestamp, _, request, \
                status_code, file_size = line.split()
        except ValueError:
            continue
        if request != 'GET /projects/260 HTTP/1.1':
            continue
        try:
            file_size = int(file_size)
            status_code = int(status_code)
        except ValueError:
            continue
        LINES_PROCESSED += 1
        TOTAL_FILE_SIZE += file_size
        if status_code in STATUS_CODES:
            STATUS_CODES[status_code] += 1
        if LINES_PROCESSED % 10 == 0:
            print(f"File size: {TOTAL_FILE_SIZE}")
            for code in sorted(STATUS_CODES.keys()):
                if STATUS_CODES[code] > 0:
                    print(f"{code}: {STATUS_CODES[code]}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {TOTAL_FILE_SIZE}")
    for code in sorted(STATUS_CODES.keys()):
        if STATUS_CODES[code] > 0:
            print(f"{code}: {STATUS_CODES[code]}")
