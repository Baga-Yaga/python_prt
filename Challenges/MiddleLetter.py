'''
Challenge
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
'''
from math import floor


# atharva
def mid(word):
    middle = 1+len(word)/2
    if middle.__float__():

        print(middle)

mid('atharvaa')