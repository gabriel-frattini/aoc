#!/usr/bin/env bash

while read line; do
  middle_len=$((${#line}/2))

  left=${line:0:$middle_len}
  right=${line:$middle_len}

  for (( i=0; i<$middle_len; i++ )) do
		for (( k=0; k<$middle_len; k++ )) do
      if [[ ${left:$i:1} == ${right:$k:1} ]]; then
        same=${left:$i:1}
      fi
		done
	done

  digit=$(printf "%d" "'$same")
  if [[ $digit -gt 96 ]]; then
    ord=$((digit-96))
  else
    ord=$((digit-38))
  fi

  sum_of_same=$((sum_of_same+ord))
done < input.txt

echo $sum_of_same

