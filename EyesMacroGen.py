import random

verbose = False #set to true for debugging prints

ignore1 = random.randint(4,7)#get first 2 players to mark.
ignore2 = random.randint(4,7)

while ignore2==ignore1:     #checks if the randoms picked the same player, if true rerolls until false.
    ignore2 = random.randint(4,7)
    if verbose == True:
        print("looping2 " + str(ignore2))

ignore3 = random.randint(2,7) #gets the second 2 players to mark.
ignore4 = random.randint(2,7)

while ignore3==ignore1 or ignore3==ignore2: #now checks to see if 3 is a repeat of 1 or 2
    ignore3 = random.randint(2,7)
    if verbose == True:
        print("looping3 " + str(ignore3))

while ignore4==ignore1 or ignore4==ignore2 or ignore4==ignore3: #checks to see if 4 is a repeat of 1 2 or 3
    ignore4 = random.randint(2,7)
    if verbose == True:
        print("looping4 " + str(ignore4))

#TODO Make a set of applicable players based on players already picked instead of just randint(1-8). Won't matter in scope of program but better & more efficient in long run.

ignore5 = random.randint(1,8) #last set of players
ignore6 = random.randint(1,8)

while ignore5==ignore1 or ignore5==ignore2 or ignore5==ignore3 or ignore5==ignore4: #last set of checks
    ignore5 = random.randint(1,8)
    if verbose == True:
        print("looping5 " + str(ignore5))

while ignore6==ignore1 or ignore6==ignore2 or ignore6==ignore3 or ignore6==ignore4 or ignore6==ignore5:
    ignore6 = random.randint(1,8)
    if verbose == True:
        print("looping6 " + str(ignore6))

print("/mk ignore1 <" + str(ignore1) + ">")
print("/mk ignore2 <" + str(ignore2) + "> <wait.5>")
print("/mk ignore1 <" + str(ignore3) + ">")
print("/mk ignore2 <" + str(ignore4) + "> <wait.5>")
print("/mk ignore1 <" + str(ignore5) + ">")
print("/mk ignore2 <" + str(ignore6) + "> <wait.5>")
print("/mk ignore1 <me>")
print("/mk ignore2 <me> <wait.1>")
print("/mk off <me>")