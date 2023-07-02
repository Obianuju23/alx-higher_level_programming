#!/bin/bash
#Script that sends DELETE request to URL,passed as 1st arg&displays response
curl -sX DELETE "$1"
