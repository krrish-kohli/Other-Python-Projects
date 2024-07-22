from replit import clear
import random
import art
from game_data import data

FOLLOWERS = 0
SCORE = 0
assume_right = True

def random_person():
	"""Chooses a random number and uses it as index for the list. So that it can choose random person and their data."""
	list_index = random.choice(data)

	global FOLLOWERS
	FOLLOWERS = list_index['follower_count']
	return f"{list_index['name']}, {list_index['description']}, from {list_index['country']}."

# Print logo
print(art.logo)

# Assigning person A and person B
A = random_person()
A_FOLLOWERS = FOLLOWERS

B = random_person()
B_FOLLOWERS = FOLLOWERS
while A == B:
	B = random_person()
	B_FOLLOWERS = FOLLOWERS

# Continue as long as user is write and update the score
while assume_right:
	print("Compare A: " + A)
	print(art.vs)
	print("Against B: " + B)
	# Take user input about who has more followers
	answer = input("Who has more followers? Type 'A' or 'B': ").upper()
	
	# Check if user's answer is correct or not
	if (answer == "A" and A_FOLLOWERS > B_FOLLOWERS) or (answer == "B" and B_FOLLOWERS > A_FOLLOWERS):
		clear()
		print(art.logo)
		SCORE += 1
		print(f"You're right! Current score: {SCORE}")
		if answer == "A":
			A = B
			A_FOLLOWERS = B_FOLLOWERS
			B = random_person()
			B_FOLLOWERS = FOLLOWERS
			while A == B:
				B = random_person()
				B_FOLLOWERS = FOLLOWERS
		else:
			B = random_person()
			B_FOLLOWERS = FOLLOWERS
			while A == B:
				B = random_person()
				B_FOLLOWERS = FOLLOWERS
			# A = B
			# A_FOLLOWERS = B_FOLLOWERS
			# B = random_person()
			# while A == B:
			# 	B = random_person()
			# B_FOLLOWERS = FOLLOWERS
	else:
		clear()
		print(art.logo)
		print(f"Sorry, that's wrong. Final score: {SCORE}")
		assume_right = False
