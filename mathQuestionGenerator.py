import random

nums = []
nums = [None] * 2

wantInstruc = ""
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
wantInstruc = input("Type 'i' for further instructions, enter any other value to continue: ")
if wantInstruc == "i":
    print("""\nInstructions:
    The number of practice questions should be greater than 0.
    The absolute value of numbers generated will be the min. negative and max. positive value randomly generated in questions.
    Questions should be answered without spaces between values.
    Answer division questions using '/' in improper fractions, and reduce to the lowest terms.\n""")

while not isinstance(numQs, int):
    numQs = input("How many practice questions?: ")
    numQs = isValidInput(numQs, 1)

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
        
    submis = input("\nType the answer: ")
    
    if opNum == 4 and "/" in submis:
        submisList = submis.split("/")
        submisList[0] = isValidInput(submisList[0], None)
        submisList[1] = isValidInput(submisList[1], None)
        submis = int(submisList[0])/int(submisList[1])
    else:
        submis = isValidInput(submis, None)
    
    if answer == submis:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        
print("\nScore: " + str(score) + "/" + str(numQs))