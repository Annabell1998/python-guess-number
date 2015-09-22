# Aqui escribe tu codigo

from random import randrange

numero_aleatorio = randrange(1, 20) #Esta es la variable donde se guarda el numero aleatorio

#count = 0 Nos servira en el ciclo While donde verificaremos To high y To Low

adivina=int(raw_input("Enter a number from 1 to 20 :")) #numero que ingresa el usuario
if adivina <=0:
	print"your number is lower to 1"
elif adivina>20:
	print "the number you entered is greater than 20"
elif adivina > numero_aleatorio:
 	print "you guess a number to high, please try again"
elif adivina < numero_aleatorio:
	print "you guess a number to low ,please try aganin"
