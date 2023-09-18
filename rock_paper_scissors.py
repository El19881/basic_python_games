import random

print("Welcome to rock, paper, scissors game!\n You will need to provide your choice of rock, paper or scissors and compete with the program. Best of 3 wins, good luck!")

def user_select():
	user_selection = input("Provide your selection. Type:\n 1: Rock\n 2: Paper\n 3: Scissors\n Your selection: ")
	return user_selection
		
def computer_select():
	computer_selection = random.randrange(1,3)
	return computer_selection

def main_loop():
	computer_wins = 0
	player_wins = 0
	while (computer_wins != 3) and (player_wins < 3):
		computer_selection = computer_select()
		user_selection = user_select()
		if (user_selection != "1") and (user_selection != "2") and (user_selection != "3"):
			print("You did not provide a valid vaue. Please try again.")
		elif computer_selection == 1 and user_selection == "2":
			print("Player won! Paper beats rock.")
			player_wins += 1
		elif computer_selection == 1 and user_selection == "3":
			print("Program won! Rock beats scissors")
			computer_wins += 1
		elif computer_selection == 1 and user_selection == "1":
			print("It is a tie!")
		elif computer_selection == 2 and user_selection == "3":
			print("Player won! Scissors beat paper.")
			player_wins += 1
		elif computer_selection == 2 and user_selection == "2":
			print("It's a tie!")
		elif computer_selection == 2 and user_selection == "1":
			print("Program won! Paper beats rock")
			computer_wins += 1
		elif computer_selection == 3 and user_selection == "1":
			print("Player won! Rock beats scissors")
			player_wins += 1
		elif computer_selection == 3 and user_selection == "3":
			print("It's a tie!")
		elif computer_selection == 3 and user_selection == "2":
			print("Program won! Scissors beat paper")
			computer_wins += 1
	if computer_wins == 3:
		print("The computer won the game with 3 wins!")
	elif player_wins == 3:
		print("The player won the game with 3 wins!")
	

main_loop()
