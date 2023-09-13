#add counter for tries
#add counter to responses
#add error handling when value provided is not integer

import random

print("Welcome to the 'Guess the number!' game! If your guess will be wrong, we will provide you hints, let's see how many tries you need!")

number = random.randrange(0,10)

user_try = int(input("Provide a number: "))

while number != user_try:
	if number > user_try:
		print("Your number is too small!")
		user_try = int(input("Provide a number: "))
	elif number < user_try:
		print("Your number is too high!")
		user_try = int(input("Provide a number: "))

if number == user_try:
	print("You won! Congratulations!")
