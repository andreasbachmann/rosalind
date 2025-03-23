#!/bin/env python3
# Given: Two DNA strings x and y of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(x,y) (number of symbols that differ in sequence).
import sys

def count_pMutations(file_path):
    with open(file_path, 'r') as file:
        x, y = file.read().splitlines()
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1     
    return count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    print(count_pMutations(file_path))