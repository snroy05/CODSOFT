import random

user_action = input("Enter a choice (Rock, Paper, Scissors): ")
possible_actions = ["Rock" , "Paper" , "Scissors"]

computer_action = random.choice(possible_actions)
print(f"\nYou chose { user_action }, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f" Both players selected {user_action}. It is a tie! ")

elif user_action == "Rock" and computer_action == "Scissors":
    print( "Rock smashes Scissors!     YOU WIN! ")

elif user_action == "Paper" and computer_action == "Rock" :
    print( "Paper covers Rock!      YOU WIN! ")

elif user_action == "Scissors " and computer_action == "Paper" :
    print( "Scissors cuts paper!    YOU WIN! ")

else:
    print( " COMPUTER WINS ")






          

