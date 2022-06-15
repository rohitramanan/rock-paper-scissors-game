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
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
elif player_choice == 2:
  print(scissors)
else:
  print("Please input a valid number.")

computer_options = [rock, paper, scissors]
computer_choice = random.choice(computer_options)
print(f"The computer chose:\n {computer_choice}")

if computer_choice == paper and player_choice == 1:
  print ("This was a draw, try again.")
if computer_choice == rock and player_choice == 0:
  print ("This was a draw, try again.")
if computer_choice == scissors and player_choice == 2:
  print ("This was a draw, try again.")
if computer_choice == rock and player_choice == 2:
  print ("You lost. Better luck next time.")
if computer_choice == rock and player_choice == 1:
  print("You won. Congratulations.")
if computer_choice == paper and player_choice == 0:
  print ("You lost. Better luck next time.")
if computer_choice == paper and player_choice == 2:
  print("You won. Congratulations.")
if computer_choice == scissors and player_choice == 0:
  print("You won. Congratulations.")
if computer_choice == scissors and player_choice == 1:
  print("You lost. Better luck next time.")