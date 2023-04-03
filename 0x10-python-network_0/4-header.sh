#!/bin/bash
#send a GET request to $1,and displays the body of the response also send a header variable
curl -s -H "X-School-User-Id: 98" "$1"
