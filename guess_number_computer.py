import random

print("Welcome to the 'Guess the number!' game!\nIf your guess will be wrong, we will provide you hints, let's see how many tries you need!")

number = random.randrange(1,2)
tries = 0

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

main_loop()
