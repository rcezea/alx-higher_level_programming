#!/bin/bash
# sends a JSON POST and displays the body of the response
curl -sX POST $1 -H 'Content-type: application/json' -d @$2
