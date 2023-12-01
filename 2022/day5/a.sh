#! /bin/bash

INPUT=input.txt

# The line below the initial stack of crates, including the stack number
INITIALCRATES=$(grep -n -e "^$" $INPUT | awk -F ":" '{print $1}')
echo $INITIALCRATES
# The line including the number of stacks
let STACKLINE=$INITIALCRATES-1
NUMOFSTACKS=$(sed -n -e "${STACKLINE}p" $INPUT | awk '{print $NF}')

# Painful parsing of file to get each stack into an element of an array
# Array elements will be started by a "^" character to ensure "empty" stacks
# still have a non-empty string representation in the array
STACK=0
STACKS=$(
    while [ $STACK -lt $NUMOFSTACKS ]
    do
        echo "^"
        head -n $(( STACKLINE-1 )) $INPUT \
            | sed -e "s/    / [ ]/g" -e "s/ //g" \
            | awk -F "]" "{print \$$(( STACK+1 ))}" \
            | sed -e "s/\[//g"
        echo ","
        let STACK+=1
    done | tr -d "\n" | tr "," " "
)
STACKS=( $STACKS )

# Get each instruction line, replacing spaces with commas so bash interprets
# each line as a single string
for INSTRUCTION in $(tail -n +$(( INITIALCRATES+1 )) $INPUT | tr " " ",")
do
    # awk columns to parse instructions
    # Stacks are 0 indexed
    # NUMCRATES is offset by 1, the "^" character that ensures no empty stacks
    let NUMCRATES=$(echo $INSTRUCTION | awk -F "," '{print $2}')
    let INITSTACK=$(echo $INSTRUCTION | awk -F "," '{print $4}')-1
    let ENDSTACK=$(echo $INSTRUCTION | awk -F "," '{print $6}')-1

    # Use bash parameter expansions to move N crates from one stack to another, ie,
    # move substrings from the beginning of one array element to another
    # Mind the padded "^"
    MOVEDCRATES=${STACKS[$INITSTACK]:1:$NUMCRATES}
    STACKS[$INITSTACK]=^${STACKS[$INITSTACK]:$((NUMCRATES+1))}
    STACKS[$ENDSTACK]=^$(echo ${MOVEDCRATES}| rev)${STACKS[$ENDSTACK]:1}
done

# Grab the second element of each string (recall the padded "^")
for STACK in ${STACKS[@]}; do echo ${STACK:1:1}; done | tr -d "\n" && echo ""
