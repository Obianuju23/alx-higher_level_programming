#!/usr/bin/bash
#A Script  that takes URL, sends request and displays response's body size
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
