import random
import sys
from string import Template

rNum = random.randrange(1,100)
def num_guessing_game(answer, rNum):
    answer = int(answer)
    # print(answer, rNum)
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


for x in range(6):
    numberOfTries = 5-x
    if numberOfTries == 5:
        print('\nPick a number between 1-100? \nYou have %s tries to guess the correct number.'%(numberOfTries,))
    elif numberOfTries == 1:
        print('\nPick a number between 1-100? \nLast one, make it count.')
    elif numberOfTries == 0:
        print('GAME OVER!!')
        break
    else:
        print('\nPick a number between 1-100? \nYou have %s tries left.'%(numberOfTries,))
            
    player_guess = sys.stdin.readline()
    try:
        player_guess = int(player_guess)
        num_guessing_game(player_guess, rNum)
    except:
        print("fuck you give me a number")
    if player_guess == rNum:
       break
