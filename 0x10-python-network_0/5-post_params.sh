#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -d "email=test@gmail%2Ecom&subject=I+will+always+be+here+for+PLD" -X POST $1