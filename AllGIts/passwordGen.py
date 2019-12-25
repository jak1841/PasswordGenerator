#!/usr/bin/env python 
import random
import os
import time

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

#return boolean if password length less than number of letters and number
def canpasswordGen(length,numletters,numnumbers):
 if(length < numletters+numnumbers):
  return False
 else:
  return True

def main():
 #Ask User again if the amount of letters and numbers are not less than 
 #password length
 length = askuserLengthpswrd()
 numletters = askuserHowmanyletters()
 numnumbers = askuserHowmanynumbers()
 while(canpasswordGen(length,numletters,numnumbers)==False):
  print("Error amount of number and letter exceeded password length")
  time.sleep(2)
  os.system("clear")
  length = askuserLengthpswrd()
  numletters = askuserHowmanyletters()
  numnumbers = askuserHowmanynumbers()

 password = " "
 for x in range(1, length):
  #Takes priority of the amount of letters and numbers person wants
  if(numletters > 0 or numnumbers >0):
   rnum2 = randomgenerator(1,2)
   if(rnum2 == 1):
    if(numletters >0):
     password = password + RandomLetters()
     numletters = numletters - 1
    else:
     password = password + str(RandomNumbers())
     numnumbers = numnumbers -1 
   else:
    if(numnumbers >0):
     password = password + str(RandomNumbers())
     numnumbers = numnumbers -1
    else:
     password = password + RandomLetters()
     numletters = numletters -1
  #If the numbers of letters and numbers in priority are less then the length
  #of the password 
  else:
   rnum2 = randomgenerator(1,2)
   if(rnum2 ==1):
    password = password + RandomLetters()
   else:
    password = password + str(RandomNumbers())
 
 print("Password: " + password)

main()



