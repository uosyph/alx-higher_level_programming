#!/bin/bash
# Sends a request to a given URL and displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d ' ' -f2
