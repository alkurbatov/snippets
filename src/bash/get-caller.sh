#!/bin/bash
#
# Determine name of the process which called this script.

CALLER=$(ps ax | grep "^ *$PPID" | awk '{print $5}')

echo I was called by \'"${CALLER}"\'
