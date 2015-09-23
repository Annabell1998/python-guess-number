"""This is a comentary"""
import random
#This is the variable where is stored the random number
try:
    NUMBER = random.randrange(1, 21)
    print NUMBER
    GUESS = int(raw_input("Enter a number from 1 to 20: "))
    #number that enters the user
    if GUESS <= 0 or GUESS > 20:
        print "You need to enter a number between 1 to 20"
    elif GUESS > NUMBER:
        print "you guess a number to high, please try again"
    elif GUESS < NUMBER:
        print "you guess a number to low, please try again"
    elif GUESS == NUMBER:
        print "You win"
except ValueError:
    print "You don't know what is a number?"

