#!/bin/bash
# A script that prints You got me! from the server
curl -sL -X PUT -H 'You got me!' 0.0.0.0:5000/catch_me_3
