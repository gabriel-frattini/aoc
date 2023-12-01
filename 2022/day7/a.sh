#!/usr/bin/env bash


cat input.txt | tr -d '$' | tr -d 'ls' | sed '/^[[:blank:]]*$/ d' | sed 's/[0-9] .*$//' | sed 's/^ *//' | paste -sd, - | xargs >> input.tmp
