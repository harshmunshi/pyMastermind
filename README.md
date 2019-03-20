# pyMastermind
A very simple implementation of mastermind in python.

## How to Run
1. Clone the repo on your local.
2. Run the following command

```
$ python mastermind.py
```

This should prompt the following guide

 Mastermind or Bulls and Cows is a popular math game in India. There is a four digit number selected by the 
	computer at random and you need to make a guess. For each number present and NOT IN It's position you get a bull and
 	if the number is present and in it's correct position you get a cow 
	-------------------------------------------------------------------------------------------------------------------
 	Some Examples 
 	Predicted 	 Actual 	 Returns 
 	1324 		 1234 		 2 Bulls 2 Cows 
 	1874 		 1234 		 0 Bulls 2 Cows 
 	giveup 	 shows you the answer 
 	-------------------------------------------------------------------------------------------------------------------- 
	THE COMPUTER HAS ALREADY PUT THE NUMBER OUT PLEASE START GUESSING THE NUMBER 

Please put you four number using space:1 2 3 4 (for example)

## Rules

1. You guess a 4 digit unique number with spaces.
2. For each number present and NOT IN It's position you get a bull.
3. For each number present and IN It's position you get a cow.
4. WHen you have 4 cows you win.
5. You can get the answer if you are not getting it by the command "giveup".
