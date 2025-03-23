#!/bin/bash
# Given: A DNA string having length at most 1000 nt.
# Return: The transcribed RNA string.
echo $(sed 's/T/U/g' data/RNA-transcribing-DNA.txt)
