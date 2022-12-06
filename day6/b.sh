#!/usr/bin/env bash


input=$(cat input.txt)
chars_count=13
count=0

for (( i=0; i<${#input}; i++ )); do
  chars_count=$((chars_count+1))

  chars=""
  slice="${input:i:14}"
  chars+="${slice:0:1}"

  for (( j=1; j<${#slice}; j++ )); do
  
    char="${slice:j:1}"

    if [[ $chars =~ "$char" ]]; then
        continue
    fi

    chars+="$char"
  done

  if [[ ${#chars} -eq 14 ]]; then
    break
  fi
done

echo "answer: $chars_count"


