""" Pangram detection

    Pangram is asentence which contains all alphabets atleast one time

REMARK I SAW THE SOLUTION IS GREEKSFORGEEKS
"""
"""
def is_pangram(string):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char not in string.lower():
            return False
    return True
"""

#CLEVER

import string
def pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())     #Comparison between set and string


print(pangram(input("Enter a string")))
