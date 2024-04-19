import random
target=random.randint(1,100)

while True:
    usernumber=input("Enter any number between 1 to 100 or quit(Q)\n")
    if(usernumber=="Q"):
        break

    usernumber=int(usernumber)
    if(usernumber==target):
        print("Right Guess")
        break
    if(usernumber<target):
        print("guess something bigger than this")
    if(usernumber>target):
        print("guess something lesser than this")

print("------GAME OVER ------")