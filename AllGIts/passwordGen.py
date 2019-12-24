#!/usr/bin/env python 
import random

print("Hello world")

#Random Function with upper and lower
def randomgenerator(lowerbound,upperbound):
 rnum = random.randint(lowerbound,upperbound)
 return rnum

for x in range (26):
 print(randomgenerator(1,26))
