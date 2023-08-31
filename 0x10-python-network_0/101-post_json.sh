#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file
curl -sX POST "$1" -d @"$2" -H "Content-Type: application/json"
