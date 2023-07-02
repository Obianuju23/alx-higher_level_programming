#!/bin/bash
#Script that takes URL,sends POST request to passed URL&display response body
curl -sd "email=test@gmail.com" -sd "subject=I will always be here for PLD" "$1"
