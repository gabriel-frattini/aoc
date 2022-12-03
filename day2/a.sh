#!/usr/bin/env bash

cat input.txt | sed 's/ /+/' \
  | sed 's/\(A+Y\|B+Z\C+X\)/6+\1/' \
  | sed 's/\(A+Z\|B+X\C+Y\)/0+\1/' \
  | sed 's/\(A+X\|B+Y\C+Z\)/3+\1/' \
  | tr 'ABCXYZ' '000123' | bc | paste -sd+ - | bc




