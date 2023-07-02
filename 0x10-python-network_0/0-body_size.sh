#!/bin/bash
#A Script  that takes URL, sends request and displays response's body size
curl -s "$1" | wc -c
