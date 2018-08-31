def isPalindrome(myText):
    text1 = ""
    text2 = ""
    string_length = len(myText)


    if (string_length%2 == 0):
        #print ("Even")
        for i in range(0,int(string_length/2)):
            text1 = myText[i] + text1
        text2 = myText[int(string_length/2): int(string_length+1)]

        #print("Text1: " + text1)
        #print ("Text2: " + text2)

        if (text1 == text2):
            return True
        else:
            return False

    else:
        #print("Odd")
        for i in range(0, int( (string_length - 1) / 2)):
            text1 = myText[i] + text1
        text2 = myText[int(string_length/2)+1: int(string_length+1)]

        #print("Text1: " + text1)
        #print ("Text2: " + text2)

        if (text1 == text2):
            return True
        else:
            return False
