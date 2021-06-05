#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:53:57 2021

@author: brianna
"""

import random

nums = []
nums = [None] * 2

opNum = 0
opSym = ""
score = 0
numQs = None
rangeInts = None

def calcAns():
    if opNum == 1:
        print(str(nums[0]) + " + " + str(nums[1]), end="")
        return nums[0] + nums[1]
    elif opNum == 2:
        print(str(nums[0]) + " - " + str(nums[1]), end="")
        return nums[0] - nums[1]
    elif opNum == 3:
        print(str(nums[0]) + " × " + str(nums[1]), end="")
        return nums[0] * nums[1]
    elif opNum == 4:
        print(str(nums[0]) + " ÷ " + str(nums[1]), end="")
        return nums[0] / nums[1]
    
def isValidInput(testVal, minVal):
    try: 
        int(testVal)
        isInt = True
    except ValueError:
        isInt = False
    
    if isInt and (minVal == None or int(testVal) >= minVal):
        return int(testVal)
    else:
        print("Invalid Value.")

print("\n..........Simple Operations Practice.........")
while not isinstance(numQs, int):
    numQs = input("How many practice questions?: ")
    numQs = isValidInput(numQs, 0)

while not isinstance(rangeInts, int):
    rangeInts = input("Greatest absolute value of numbers generated?: ")
    rangeInts = isValidInput(rangeInts, 0)
    

for i in range(numQs):
    opNum = random.randint(1, 4)
    
    nums[0] = random.randint(-rangeInts, rangeInts)
    nums[1] = random.randint(-rangeInts, rangeInts)
    
    if opNum == 4:
        while (nums[1] == 0):
            nums[1] = random.randint(-rangeInts, rangeInts)
    
    answer = None
    
    print("\nQuestion " + str(i + 1) + ": ", end="")
    
    answer = calcAns()
        
    submis = input("Type the answer: ")
    
    if opNum == 4 and "/" in submis:
        submisList = submis.split("/")
        submis = int(submisList[0])/int(submisList[1])
    
    submis = isValidInput(submis, None)
    
    if answer == submis:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        
print("\nScore: " + str(score) + "/" + str(numQs))