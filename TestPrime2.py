import random
x = 0
found = True
firstPrime = 0
firstRandomNumber = 0
checkPrime = False

secondPrime = 0
secondRandomNumber = 0


z = 0
def checkP(x):
    b = 2
    foundPrime = True
    while foundPrime:
        if x % b == 0:
            if x != b:
                foundPrime = False
            if x == b:
                print(x)
                foundPrime = False
                return True
        b = b + 1
    b = 2


while found:
    x = random.randrange(5000, 6000)
    print("this is the value             ",x)
    checkPrime = checkP(x)
    if checkPrime:

        if z == 0:
            firstPrime = x

            print("first prime ",firstPrime)
        if z == 1:
            secondPrime = x

        print("second prime",secondPrime)
        if z == 2:
            firstRandomNumber = x
        if z == 3:
            secondRandomNumber = x
            found = False
        z = z + 1

print("first prime",firstPrime)
print("second prime",secondPrime)
print("first random number ",firstRandomNumber)
print("second random number",secondRandomNumber)

Alice = firstPrime ** firstRandomNumber % secondPrime
print("Alice",Alice)
Bob = firstPrime ** secondRandomNumber % secondPrime
print("Bob",Bob)


NewAlice = Bob ** firstRandomNumber % secondPrime
newBob = Alice ** secondRandomNumber % secondPrime
if NewAlice == newBob:
    print("ok")
    print("NewAlice",NewAlice,"newBob",newBob)



