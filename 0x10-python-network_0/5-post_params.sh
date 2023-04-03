#!/bin/bash
#send a POST with two url parameters email and subject to $1,and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
