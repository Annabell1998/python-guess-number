"""This is a comentary"""
import random
import os, sys
#This is the variable where is stored the random number
count = 0
NUMBER = random.randrange(1, 21)
while count <= 3:
    try:
        print NUMBER
        print ""
        print ""
        print ""
        print"-------------------------------"
        GUESS = int(raw_input("Enter a number from 1 to 20: "))
        count = count + 1
        #number that enters the user
        if GUESS <= 0 or GUESS > 20:
            print "You need to enter a number between 1 to 20"
        elif GUESS > NUMBER:
            print "you guess a number to high, please try again"
        elif GUESS < NUMBER:
            print "you guess a number to low, please try again"
        elif GUESS == NUMBER:
            print "You win"
            sys.exit()
        else:
        	count > 3
        	sys.exit()
    except ValueError:
        print "You don't know what is a number?"