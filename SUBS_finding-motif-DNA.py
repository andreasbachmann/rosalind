#!/bin/env python3
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.
import sys

def find_motif(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        DNA = lines[0].strip()
        motif = lines[1].strip()

        if len(DNA) < len(motif):
            return "Motif is longer than DNA sequence"
        elif len(DNA) >= len(motif):
            motif_positions = []
            for i in range(len(DNA)):
                if DNA[i:i+len(motif)] == motif:
                    motif_positions.append(i+1)
        
    return motif_positions

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    print(find_motif(file_path))