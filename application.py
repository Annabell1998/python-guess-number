from random import randrange


random_number = randrange(1, 21) #This is the variable where is stored the random number

try:
	guess=int(raw_input("Enter a number from 1 to 20: ")) #number that enters the user
	if guess <=0 or guess > 20:
		print"You need to enter a number between 1 to 20"
	elif guess > random_number:
 		print "you guess a number to high, please try again"
	elif guess < random_number:
		print "you guess a number to low ,please try again"

except:
	print "You don't know what is a number?"
