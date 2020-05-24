import math
import os
import random
import re
import sys

def maxOnes(n):
    count = 0
    while (n!=0):
        n = (n & (n << 1))
        count=count+1
    return count

if __name__ == '__main__':
    n = int(input())
    max_ones = maxOnes(n)
    print(max_ones)
    
#Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n .
