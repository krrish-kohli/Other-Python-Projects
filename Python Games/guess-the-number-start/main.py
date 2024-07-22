#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

is_not_right = False
LIVES = 0

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
# print(f"The number is: {random_number}")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def life_counter():
	global LIVES
	global is_not_right
	print(f"You have {LIVES} attempts remaining to guess the number.")
	while not is_not_right:	
		guessed_number = int(input("Make a guess: "))
		LIVES -= 1
		if LIVES == 0:
			print("You've run out of guesses, you lose.")
			is_not_right = True
		else:
			if guessed_number == random_number and LIVES > 0:
				print(f"You got it! The answer was {random_number}.")
				is_not_right = True			
			else:
				if guessed_number > random_number:
					print("Too high.")
				else:
					print("Too low.")
					
				print("Guess again.")
				print(f"You have {LIVES} attempts remaining to guess the number.")


if difficulty_level == "easy":
	LIVES = 10
	life_counter()
elif difficulty_level == "hard":
	LIVES = 5
	life_counter()

else:
	print("Please select a valid difficulty")