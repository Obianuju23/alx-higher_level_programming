#!/bin/bash
#Script that sends DELETE request to URL,passed as 1st arg&displays response
curl -Xs DELETE "$1"
