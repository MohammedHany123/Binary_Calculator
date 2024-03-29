# -*- coding: utf-8 -*-
"""Binary Calculator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NNUi_2dfgGEblSRoPXZwsKPNn9BmN5_T
"""

#Prepared By:
#Ahmed Samir
#Mohammed Hany
#Loay Medhat

#a function to check that the input number is a valid binary number
def checkNumber(num):
    #loop through the number string and if there is a digit not equal to 1 or 0 return False
    for i in range(len(num)):
        if num[i] != '0' and num[i] != '1':
            return False

#a function to get the 1's complement of a binary number
def oneComplement(num):
    result = ""
    #loop through the number string and converts 0s to 1s and vice versa then add it to result string
    for i in range(len(num)):
        if num[i] == "0":
            result += "1"
        else:
            result += "0"
    return result

#a function to get the 2's complement of a binary number
def twoComplement(num):
    result = ""
    #loop through the number string starting from the LSB and when found a 1, flip the other bits on left.
    index = 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == "1":
            #get the index of the first 1 bit
            index = i
            break
    #1's complement is the same idea of flipping the bits
    result = oneComplement(num[:index]) + num[index:]
    return result

#a function to make an addition operation between two binary numbers
def addition(num1, num2):
    result = ""
    #carry varaible to store whether there is a carry within the addition variable
    carry = 0
    #make a while loop by passing over every number and add its value to total variable
    i = len(num1)-1
    j = len(num2)-1
    while i >= 0 or j >= 0 or carry:
        #assign the value of carry to total at the beginning of each iteration
        total = carry
        #loop through num1 and add the integer value of each digit to the total
        if i >= 0:
            total += int(num1[i])
            i -= 1
        #loop through num2 and add the integer value of each digit to the total
        if j >= 0:
            total += int(num2[j])
            j -= 1
        #1+1 = 0, this can be replaced by total%2 as 2%2 = 0 and 1%2 = 1
        result += str(total%2)
        #if total is more than 1 it will have a carry.
        carry = total//2
    result = result[::-1]
    #check for overflow
    if len(result) > len(num1) and len(result) > len(num2):
        return f"({result[0]}){result[1:]} an overflow occurred"
    return result

#a function to check that num2 is bigger than num1 for subtraction process
def noNegative(num1, num2):
    #check that the two numbers have the same number of bits
    if len(num1) > len(num2):
        num2 = "0"*(len(num1)-len(num2)) + num2
    elif len(num2) > len(num1):
        num1 = "0"*(len(num2)-len(num1)) + num1
    #loop through the two numbers
    #no difference between using len(num1) and len(num2) as both have the same length
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            if num1[i] == "0" and num2[i] == "1":
                return False
            elif num1[i] == "1" and num2[i] == "0":
                return True

#a function to subtract between two numbers
def subtraction(num1, num2):
    #check that the two numbers have the same number of bits
    if len(num1) > len(num2):
        num2 = "0"*(len(num1)-len(num2)) + num2
    elif len(num2) > len(num1):
        num1 = "0"*(len(num2)-len(num1)) + num1
    result = ""
    for i in range(len(num1)-1, -1, -1):
        #do subtraction between two digits seperately
        if int(num1[i])-int(num2[i]) >= 0:
            result += str(int(num1[i])-int(num2[i]))
        #when reaches the operation of 0-1, make a borrow from the adjacent bit
        else:
            #add 1 to the result string as the result from 0-1 = 1
            result += "1"
            index = i-1
            #change the adjacent bit as a result for the borrow
            if num1[index] == "1":
                num1 = num1[:index] + "0" + num1[index+1:]
            else:
                #when the adjacent bit not equals 1, continue to do borrowing from the ajacent bit
                while num1[index] != "1":
                    num1 = num1[:index] + "1" + num1[index+1:]
                    index -= 1
                num1 = num1[:index] + "0" + num1[index+1:]
    result = result[::-1]
    return result

#Display Menu 1
print("** Binary Calculator ** \nA) Insert new numbers \nB) Exit")

#Take the input from the user and make a loop to do the process until the user says else
#if the user input a lowercase letter, the program will deal with it the same as uppercase
answer1 = input("Please enter your choice (A/B): ").upper()
if answer1 == "B":
    print("Exiting the program. Goodbye")

#if user input any choice but "B", it will go to make the processes or to tell him to input a valid input
while(answer1 != "B"):

    #If the user chose to insert a new number, the program will function normally
    if answer1 == "A":

        #check the validity's of the user's number
        num1 = input("please insert a number: ")
        while(checkNumber(num1) == False):
            num1 = input("please insert a valid number: ")

        #Show Menu 2 and take the input from the user
        #if the user input a lowercase letter, the program will deal with it the same as uppercase
        print("** Please select the operation ** \nA) Compute one's complement \nB) Compute two's complement \nC) Addition \nD) Subtraction")
        answer2 = input("Please enter your choice (A/B/C/D): ").upper()

        #When the user inputs an invalid input, ask him to repeat until it is valid
        while (answer2 != "A" and answer2 != "B" and answer2 != "C" and answer2 != "D"):
            answer2 = input("Please select a valid choice: ").upper()


        #based on the user's answer, do the desired operation
        if answer2 == "A":
            result = oneComplement(num1)
            print(f"result is: {result}")

        elif answer2 == "B":
            result = twoComplement(num1)
            print(f"result is: {result}")

        #if user chose operation C or D, ask him to insert another number and check its validity
        elif answer2 == "C":
            num2 = input("please insert a number: ")
            #check the validity's of the user's input
            while(checkNumber(num2) == False):
                num2 = input("please insert a valid number: ")
            #print the result for the user
            result = addition(num1, num2)
            print(f"result is: {result}")

        elif answer2 == "D":
            num2 = input("please insert a number: ")
            #check the validity of the number
            while(checkNumber(num2) == False):
                num2 = input("please insert a valid number: ")
            #check that the second number is less than the first number
            while(noNegative(num1, num2) == False):
                num2 = input("please insert a number less than the first number: ")
            #print the result for the user
            result = subtraction(num1, num2)
            print(f"result is: {result}")

    #when user inputs a choice rather than A or B for Menu 1, repeat the process from the beginning
    else:
        print("please select a valid choice")

    #after showing the result, or if the user insert a wrong value rather than A or B at first, show Menu 1 for the user again.
    print("** binary calculator ** \nA) insert new numbers \nB) Exit")
    answer1 = input("Please enter your choice (A/B): ").upper()
    if answer1 == "B":
        print("Exiting the program. Goodbye")