import random
import numpy as np 

# Generate four numbers

def generateRandomSequence(num=4):
	array = []
	total_num = 0
	while(total_num != 4):
		gen = random.randint(1,9)
		if gen in array:
			pass
		else:
			array.append(gen)
			total_num += 1
	return array

def checkBullsAndCows(prediction, array):
	bulls = 0 
	cows = 0

	for i in range(4):
		if prediction[i] == array[i]:
			cows +=1
		elif prediction[i] in array:
			bulls += 1
		else:
			pass
	return (bulls, cows)

print(" \n Mastermind or Bulls and Cows is a popular math game in India. There is a four digit number selected by the \n\
	computer at random and you need to make a guess. For each number present and NOT IN It's position you get a bull and\n \
	if the number is present and in it's correct position you get a cow \n\
	-------------------------------------------------------------------------------------------------------------------\n \
	Some Examples \n \
	Predicted \t Actual \t Returns \n \
	1324 \t\t 1234 \t\t 2 Bulls 2 Cows \n \
	1874 \t\t 1234 \t\t 0 Bulls 2 Cows \n \
	giveup \t shows you the answer \n \
	-------------------------------------------------------------------------------------------------------------------- \n\
	THE COMPUTER HAS ALREADY PUT THE NUMBER OUT PLEASE START GUESSING THE NUMBER \n")

array = generateRandomSequence(4)
while(True):
	print("Please put you four number using space:1 2 3 4 (for example) \n")
	x = raw_input("Your Guess:")

	# Preprocess the guess
	try:
		if x == "giveup":
			print("The answer was: {}".format(array))
			break
		prediction = [int(i) for i in x.split(" ")]
		bulls, cows = checkBullsAndCows(prediction, array)
		print("Result of your guess: {} bulls and {} cows".format(bulls, cows))
		print("----------------------------------------------------------------\n ")
		if cows == 4:
			print("You hit the right number BINGO!!!!")
			break
	except:
		print("Format Not Understood, please try again")
		continue