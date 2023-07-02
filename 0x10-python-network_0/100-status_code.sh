#!/bin/bash
#Scriptthat sends request pass as 1st arg&displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
