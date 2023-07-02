#!/bin/bash
#Script that takes URL,sends POST request to passed URL&display response body
#A variable email must be sent with the value test@gmail.com
#A variable subject must be sent with the value I will always be here for PLD
curl -sd "email=test@gmail.com" -sd "subject=I will always be here for PLD" "$1"
