#!/bin/bash
#curl the first argument passed to the script using $1 variable and uses word count to return the size of the response
curl -s "$1" | wc -c
