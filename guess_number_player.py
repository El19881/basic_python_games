print("Welcome to the 'Guess the number!' game!\n Player 1 will provide a random number and Player 2 will have too guess it. Let's see how many tries Player 2 will need! No peeking!")
tries = 0

def number_winner():
	try:
		number = int(input("Provide the number Player 2 will have to guess: "))
		return number
	except:
		print("You did not provide a vaid number, please provide a valid number to guess.")
		return number_winner()
		
def main_loop():
	global tries
	try:
		user_try = int(input("Provide a number: "))
		tries += 1
		while number != user_try:
			if number > user_try:
				print("Your number is too small!")
				user_try = int(input("Provide a number: "))
				tries += 1
			elif number < user_try:
				print("Your number is too high!")
				user_try = int(input("Provide a number: "))
				tries +=1
	except:
		print("You did not provide a number. Please provide a valid number")
		#tries += 1 if you would like to count non integer attempts as well
		return main_loop()
	
	if number == user_try:
		print(f"You won! Congratulations! You needed {tries} attempt(s) to guess the number!")


number = number_winner()
main_loop()
