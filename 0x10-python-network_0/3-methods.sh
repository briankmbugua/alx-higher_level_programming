#!/bin/bash
# takes in a URL and displays all HTTP methods the path accepts.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
