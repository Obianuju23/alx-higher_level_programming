#!/bin/bash
#Script that sends DELETE request to URL,passed as 1st arg&displays response
curl -s DELETE -X "$1"
