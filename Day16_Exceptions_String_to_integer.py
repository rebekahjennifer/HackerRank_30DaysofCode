Read a string,S, and print its integer value; if S cannot be converted to an integer, print Bad String.
import sys
S = input().strip()

try:
        a = int(S)
        print(a)
        
except ValueError:
        print('Bad String')
