import random
import sys

rNum = random.randrange(0,100)
def num_guessing_game(answer, rNum):
    # rNum = randomNum
    print(answer, rNum)
    if ((answer < rNum) and (rNum - answer >= 10 )):
        print("You're getting colder \nYou're too low")
    elif ((answer > rNum) and (answer - rNum >= 10 )):
        print("You're getting colder \nYou're too high")
    elif ((answer < rNum) and (rNum - answer <= 10 )):
        print("You're getting warmer \nYou're a little low")
    elif ((answer > rNum) and (answer - rNum <= 10 )):
        print("You're getting warmer \nYou're a little high")
    else:
        print("Correct! you are on fire!")
        return

num_guessing_game(2, rNum)
num_guessing_game(30, rNum)
num_guessing_game(50, rNum)
