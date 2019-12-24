#!/usr/bin/env python 
import random

#Random Function with upper and lower
def randomgenerator(lowerbound,upperbound):
 rnum = random.randint(lowerbound,upperbound)
 return rnum

#Ask User questionss
def askuserLengthpswrd():
 return input("Type Length of password: ")

def askuserHowmanyletters():
 return input("Type number of letters in password: ")

def askuserHowmanynumbers():
 return input("Type number of numbers in password: ")

def main():
 length = askuserLengthpswrd()
 numletters = askuserHowmanyletters()
 numnumbers = askuserHowmanynumbers()
 print("Length: " + str(length) + " Letters: " +str( numletters) +
 " Numbers: " +str( numnumbers)) 

main()
