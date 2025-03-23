#!/bin/bash
# Given: A DNA string of length at most 1000 bp.
# Return: The reverse complement strand.
sed 'y/ATGC/TACG/' data/REVC_complement-DNA-strand.txt | rev
