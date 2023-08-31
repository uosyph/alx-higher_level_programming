#!/bin/bash
# Sends a POST request to a given URL using curl, then displays the response
curl -s POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
