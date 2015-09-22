from random import randrange

<<<<<<< HEAD
print "Hello World"
print "mi primer commit"
=======
random_number = randrange(1, 20) #This is the variable where is stored the random number

guess=int(raw_input("Enter a number from 1 to 20 :")) #number that enters the user
if guess <=0:
	print"your number is lower to 1"
elif guess>20:
	print "the number you entered is greater than 20"
elif guess > random_number:
 	print "you guess a number to high, please try again"
elif guess < random_number:
	print "you guess a number to low ,please try again"
>>>>>>> ffc9278eddad5a8bf98267a29c6872897482b0f6
