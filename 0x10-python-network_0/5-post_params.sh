#!/bin/bash
#Script that takes URL,sends POST request to passed URL&display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
