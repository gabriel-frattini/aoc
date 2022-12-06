#!/usr/bin/env bash


input=$(cat input.txt)
chars_count=3
count=0

for (( i=0; i<${#input}; i++ )); do
  chars_count=$((chars_count+1))

  chars=""
  slice="${input:i:4}"
  chars+="${slice:0:1}"

  for (( j=1; j<${#slice}; j++ )); do
  
    char="${slice:j:1}"

    if [[ $chars =~ "$char" ]]; then
        continue
    fi

    chars+="$char"
  done

  if [[ ${#chars} -eq 4 ]]; then
    break
  fi
done

echo "answer: $chars_count"


