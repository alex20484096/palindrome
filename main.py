#!/usr/local/bin/python3

import argparse
import palindrome



parser = argparse.ArgumentParser()
parser.add_argument("text_to_check")
args = parser.parse_args()


if args.text_to_check.isalpha():
    print(palindrome.isPalindrome(args.text_to_check))
else:
    print("Please no numbers or special characters in your text")
