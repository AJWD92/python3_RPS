
"""This is a Rock, Paper, Scissors game it will ask the user to pick Rock, Paper, or Scisssors. Then the computer will randomly select one of the options and tell the user if they won or lost given the parameters of the rules"""

from random import randint
options = ["ROCK", "PAPER", "SCISSORS"]
message = {
   "tie": "Yawn it's a tie!",
   "won": "Yay you won!",
   "lost": "Aww you lost!" 
 }

def decide_winner(user_choice, computer_choice):
  print ("You selected: {}".format(user_choice)) 
  print ("Computer seleceted: {}".format(computer_choice))
  if user_choice == computer_choice:
    print (message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print (message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print (message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print (message["won"])
  else:
    print (message["lost"])

def play_RPS():
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
