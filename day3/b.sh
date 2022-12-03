#!/usr/bin/env bash

input=$(cat input.txt)
sum_of_same=0
lines=$(wc -l input.txt)
input_len=$(echo $lines | cut -d' ' -f1)


for i in  `seq 1 3 $input_len`; do
  first=$(head -"$((i))" input.txt | tail +"$((i))")
  second=$(head -"$((i+1))" input.txt | tail +"$((i+1))")
  third=$(head -"$((i+2))" input.txt | tail +"$((i+2))")
  first_len=$((${#first}))
  second_len=$((${#second}))
  third_len=$((${#third}))
  
  
  # Please forgive me.
  for (( i=0; i<$first_len; i++ )) do
		for (( j=0; j<$second_len; j++ )) do
      if [[ ${first:$i:1} == ${second:$j:1} ]]; then
        for (( k=0; k<$third_len; k++ )) do
          if [[ ${first:$i:1} == ${third:$k:1} ]]; then
            same=${first:$i:1}
          fi
        done
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
done


echo $sum_of_same
