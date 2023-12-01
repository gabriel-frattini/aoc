#!/usr/bin/env bash

input=$(cat input.txt | sed 's/,/ /' | sed 's/-/ /' | sed 's/-/ /')
answer=0

while read -r line; do

	x=$(echo "$line" | cut -d' ' -f1)
	y=$(echo "$line" | cut -d' ' -f2)
	z=$(echo "$line" | cut -d' ' -f3)
	w=$(echo "$line" | cut -d' ' -f4)

  if [[ $x -ge $z && $y -le $w ]] || [[ $y -ge $z && $y -le $w ]] || [[ $z -ge $x && $w -le $y ]] || [[ $z -le $y && $w -ge $x ]]; then
       answer=$((answer+1))
  fi
  

done <<< "$input"

echo $answer
