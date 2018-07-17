import random
import sys

rNum = random.randrange(0,100)
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


for x in range(10):
    print('What is your number?')
    player_guess = sys.stdin.readline()
    try:
        player_guess = int(player_guess)
        num_guessing_game(player_guess, rNum)
    except:
        print("fuck you give me a number")
    if player_guess == rNum:
       break
