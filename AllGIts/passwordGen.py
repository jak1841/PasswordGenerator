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

#Get Random Letters
def RandomLetters():
 rnum = randomgenerator(1,2)
 if(rnum == 1):
  random = chr(randomgenerator(65,90))
 else:
  random = chr(randomgenerator(97,122)) 
 return random

#Get Random Numbers
def RandomNumbers():
 random = randomgenerator(1,9)
 return random

def main():
 length = askuserLengthpswrd()
 numletters = askuserHowmanyletters()
 numnumbers = askuserHowmanynumbers()

 password = " "
 for x in range(1, length):
  #Takes priority of the amount of letters and numbers person wants
  if(numletters > 0 or numnumbers >0):
   rnum2 = randomgenerator(1,2)
   if(rnum2 == 1):
    password = password + RandomLetters()
   else:
    password = password + str(RandomNumbers())

 print("Length: " + str(length) + " Letters: " +str( numletters) +
 " Numbers: " +str( numnumbers)) 
 print("Password: " + password)
main()



