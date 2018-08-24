#!/usr/local/bin/python3

import sys

def isPalindrome(myText):
    array1 = []
    text1 = ""
    text2 = ""
    string_length = len(myText)


    if (string_length%2 == 0):
        print ("Even")
        for i in range(0,int(string_length/2)):
            text1 = myText[i] + text1
        print("Text1: " + text1)

        text2 = myText[int(string_length/2): int(string_length+1)]
        print ("Text2: " + text2)
    else:
        print("Odd")
        for i in range(0, int( (string_length - 1) / 2)):
            text1 = myText[i] + text1
        print("Text1: " + text1)

        text2 = myText[int(string_length/2)+1: int(string_length+1)]
        print ("Text2: " + text2)

isPalindrome(sys.argv[1])

'''
if len(sys.argv) < 2:
    print("Please provide a year as an argument")
else:
    value = sys.argv[1]
    print(isPalindrome(value))
'''
