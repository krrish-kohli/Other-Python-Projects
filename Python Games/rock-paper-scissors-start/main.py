import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#What the user chooses
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice == "0":
  print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

# What the computer chooses
print("Computer chose: \n")
shapes = [rock, paper, scissors]
computer_choice = random.choice(shapes)
print(computer_choice)

# Winner declaration according to rules
if (user_choice == "0" and computer_choice == rock) or (user_choice == "1" and computer_choice == paper) or (user_choice == "2" and computer_choice == scissors):
    print("It's a draw")
elif (user_choice == "0" and computer_choice == scissors) or (user_choice == "1" and computer_choice == rock) or (user_choice == "2" and computer_choice == paper):
    print("You win!")
else:
    print("You lose!")