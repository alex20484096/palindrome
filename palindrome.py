#!/usr/local/bin/python3

import sys

def isPalindrome(myText):
    array1 = []
    array2 = []
    string_length = len(myText)
    if (string_length%2 == 0):
        print ("Even")
        for i in range(0,int(string_length/2)):
            array1.append(myText[i])
        array1.sort()
        print("".join(array1))
    else:
        print("Odd")
        for i in range(0, int( (string_length - 1) / 2)):
            array1.append(myText[i])
        array1.sort()
        print("".join(array1))

isPalindrome(sys.argv[1])

'''
if len(sys.argv) < 2:
    print("Please provide a year as an argument")
else:
    value = sys.argv[1]
    print(isPalindrome(value))
'''
