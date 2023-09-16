#ROCK PAPER SCISORR NOW

#random number to select rock/paper/scisor for computer
#input from user for selection
#make sure there is error handling for user input
#display info who lost
#best of 3 length (add a counter)
#display overall winner
# ask if user wants to play again
#error handling for user input

import random
computer_wins = 0
player_wins = 0


print("Welcome to rock, paper, scissors game!\n You will need to provide your choice of rock, paper or scissors and compete with the program. Best of 3 wins, good luck!")

def user_select():
	user_selection = input("Provide your selection. Type:\n 1: Rock\n 2: Paper\n 3: Scissors\n Your selection: ")
	return user_selection
	if (user_selection != "1") and (user_selection != "2") and (user_selection != "3"):
		print("You did not provide a valid vaue. Please try again.")
		return user_select()
		
def computer_select():
	computer_selection = random.randrange(1,3)
	return computer_selection

def main_loop:
	while (computer_wins < 2) and (player_wins < 2):
		computer_select()
		user_select()
		if computer_selection == 1 and user_selection == "2":
			print("Player won! Paper beats rock.")
			player_wins += 1
		elif computer_selection == 1 and user_selection == "3":
			print("Program won! Rock beats scissors")
			computer_wins += 1
		elif computer_selection == 1 and user_selection == "1":
			print("It is a tie!")
