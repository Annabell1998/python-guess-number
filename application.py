"""if you enter the  correct number then the programm say : You win
and ask you if you want play again,
if you lose for four times then ask you if you want play again! """
import random
#This is the variable where is stored the random number
ANSWER = "K"
ANSWER2 = True
print "      _____                    _                   "
print "     |  __ -                  | | "
print "     | |__) | __ _  _ __    __| |  ___   _ __ ___  "
print "     |  _  / / _` || '_ -  / _` | / _ - | '_ ` _ - "
print "     | | | || (_| || | | || (_| || (_) || | | | | |"
print "     |_| |_| -__,_||_| |_| -__,_| -___/ |_| |_| |_|"
print "      _   _                    _                    _____ "
print "     | - | |                  | |                  / ____|"
print "     |  -| | _   _  _ __ ___  | |__    ___  _ __  | |  __   __ _  _ __ ___    ___"
print "     | . ` || | | || '_ ` _ - | '_ -  / _ -| '__| | | |_ | / _` || '_ ` _ -  / _ -"
print "     | |-  || |_| || | | | | || |_) ||  __/| |    | |__| || (_| || | | | | ||  __/"
print "     |_| -_| -__,_||_| |_| |_||_.__/  -___||_|     -_____| -__,_||_| |_| |_| -___|"
while ANSWER2 == True:
    COUNT = 0
    NUMBER = random.randrange(1, 21)
    while COUNT <= 3:

        try:
            COUNT = COUNT + 1
            if COUNT == 1:

                print "\n\n---------------you need to enter a number between 1 to 20---------------"
            elif COUNT == 2:
                print "\n -----------------------*****************************-------------------"
                print "\n                      You are in the turn", str(COUNT)
            elif COUNT == 3:
                print "\n -----------------------********************************----------------"
                print "\n                       You are in the turn", str(COUNT)
            elif COUNT == 4:
                print "\n -----------------------********************************-----------------"
                print "\n                       You are in the turn", str(COUNT)
            print "                  ***********Enter a number from 1 to 20**********\n"
            GUESS = int(raw_input("here: "))
            #COUNT = COUNT + 1
            #number that enters the user
            if GUESS <= 0 or GUESS > 20:
                print "\n   ****************You need to enter a number between 1 to 20************"
            elif GUESS > NUMBER:
                print "\n                you guess a number to high, please try again!!!!!!"
            elif GUESS < NUMBER:
                print "\n                you guess a number to low, please try again!!!!!!"
            elif GUESS == NUMBER:
                print "\n                       *$$$$$$$$$$ You win $$$$$$$$$*"
                COUNT = 4
        except ValueError:
            print "\n                       You don't know what is a number? xD "
            COUNT = COUNT
    print " \n\n                ************** the Answer is", str(NUMBER), "**************\n"

    while (ANSWER != "Y" or ANSWER != "y") or (ANSWER != "n" or ANSWER != "N"):
        ANSWER = raw_input("                      Do you want to play again? Y/N: ")
        if ANSWER == "Y" or ANSWER == "y":
            print "\n\n                        ***  It was nice to see you again ***\n"
            ANSWER2 = True
            break
        elif ANSWER == "n" or ANSWER == "N":
            print" \n                           ***You have left the game***\n"
            print"*Please come back soon :3 I love you , maybe I'm a robbot but i have feelings* \n"
            ANSWER2 = False

            break
