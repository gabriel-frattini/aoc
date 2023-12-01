#!/usr/bin/env bash


cat input.txt | sed 's/^[ \t]*//' | sed 's/^.*:[ \t]//' | sed 's/new = //' | sed 's/Monkey //' | sed 's/^.*://' | sed 's/throw to monkey //' | sed 's/divisible by //'
