#!/usr/bin/env python3
from random import randint
# Gambling program
player_credit = 100
while(True):
    warning = True
    order = input("Type PLAY to attempt another win, CREDIT to see how you have, QUIT to leave.")
    if (player_credit < 30 and warning):
        print("I guess you noticed now, this game's design can only make you lose.")
        print(f"You started with 100 and now have {player_credit}")
        print(f"Lesson of the day: don't play hazard games or at least choose them well!")
        warning = False
    if (order == "PLAY"):
        if (player_credit < 1):
            print("Sorry you do not have any credit left. Bye!")
            break
        coin_toss = randint(0, 1)
        bet_value = (player_credit // 2) + 1
        if coin_toss:
            player_credit += bet_value
            print(f"Congrats, you won {bet_value}! ")
        else:
            player_credit -= bet_value
            print(f"Ouch! you just lost {bet_value}")
    elif (order == "CREDIT"):
        print(f"You currently have {player_credit} credits")
    elif (order == "QUIT"):
        break
