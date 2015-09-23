"""This code is a game of random numbers"""
import random
#This is the variable where is stored the random number
ANSWER = "Y"
while ANSWER == "Y" or ANSWER == "y":
    COUNT = 0
    NUMBER = random.randrange(1, 21)
    while COUNT <= 3:
        try:
            print ""
            print ""
            print"-------------------------------"
            GUESS = int(raw_input("Enter a number from 1 to 20: "))
            COUNT = COUNT + 1
            #number that enters the user
            if GUESS <= 0 or GUESS > 20:
                print "You need to enter a number between 1 to 20"
            elif GUESS > NUMBER:
                print "you guess a number to high, please try again"
            elif GUESS < NUMBER:
                print "you guess a number to low, please try again"
            elif GUESS == NUMBER:
                print "You win"
                COUNT = 4
        except ValueError:
            print "You don't know what is a number?"
            COUNT = COUNT + 1
    ANSWER = raw_input("Do you want to play again? Y/N: ")

