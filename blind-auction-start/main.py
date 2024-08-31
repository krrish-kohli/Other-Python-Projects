from replit import clear
from art import logo

print(logo)

more_bidding = True
player_dict = {}

def max_bid():
	max_bid = 0
	max_name = ""
	for items in player_dict:
		bid_amount = player_dict[items]
		if bid_amount >= max_bid:
			max_bid = player_dict[items]
			max_name = items
	print(f"Highest bidder is {max_name} with ${max_bid}")

while more_bidding:
	name = input("What is your name?: ")
	bid = int(input("What is your bid?: $"))

	player_dict[name] = bid
	
	more_players = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
	if more_players == "yes":
		clear()
		more_bidding = True
		# data()
	else:
		more_bidding = False

	max_bid()
