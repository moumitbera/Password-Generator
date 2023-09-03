#author: @moumit
#version2.0: for user defined length

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generatePassword():
    length = int(input("Enter the length of the password you need: "))
    if length < 8:
        print("The password is too short. Make it lengthy")
    else:
        numSymbol = random.randint(2, length-4)
        numLetter = random.randint(2, length-(numSymbol+2))
        numDigits = random.randint(2, length-(numSymbol+numLetter))

        password = ""

        #for symbols
        for i in range(0, numSymbol):
            password = password + random.choice(symbols)
    
        for i in range(0, numLetter):
            password = password + random.choice(letters)
    
        for i in range(0, numDigits):
            password = password + random.choice(digits)

        passwordAsList = []
        for i in password:
            passwordAsList.append(i)

        #randomly arranging password
        finalPassword = ""
        for i in range(0, length):
            finalPassword = finalPassword + random.choice(passwordAsList)
    
        print(f"Password Generated is {finalPassword}")

generatePassword()
