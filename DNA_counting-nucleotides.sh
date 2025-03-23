#!/bin/bash
# Given: A DNA string of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in the DNA string.
echo $(grep -o 'A' data/DNA_counting-nucleotides.txt | wc -l) $(grep -o 'C' data/DNA_counting-nucleotides.txt | wc -l) $(grep -o 'G' data/DNA_counting-nucleotides.txt | wc -l) $(grep -o 'T' data/DNA_counting-nucleotides.txt | wc -l)
