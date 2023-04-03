#!/bin/bash
# DELETE request to URL in arg $1 and displays the body of the response
curl -s -X DELETE "$1"
