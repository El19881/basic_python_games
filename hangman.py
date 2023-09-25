#player1 input word
#player2 input letter
#check if letter in word
#if not add to the hangman
#display wrong letters and correct letters
#board for good letters?
#hangman build:multiline string?
# add .upper() zeby zawsze patrzec na to samo niezaleznie od kapitalizacji
# add logic for word input to check validity (no spaces or dashes in the word)


def hangman():
	guess_word_input = input("Please provide the word the player will need to guess: ")
	word_letters = set(guess_word_input) #letters in the word to guess
	word = guess_word_input
	provided_letters = set() #letters user has used as guesses
	letters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
	hangman_status = 0
	hangman = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]

	
	#getting user input
	while len(word_letters) > 0 and hangman_status != 11:
		#letters used
		print("You have used so far: ", ','.join(provided_letters))
		#what is the current status of letters guessed with dashes: W-O-G (WRONG)
		word_list = [letter if letter in provided_letters else "-" for letter in guess_word_input]
		print("The word to guess is: ", ' '.join(word_list))

		
		player_guess_letter = input("Please provide a letter: ")
		if player_guess_letter in letters - provided_letters:
			provided_letters.add(player_guess_letter)
			if player_guess_letter in word_letters:
				word_letters.remove(player_guess_letter)
			else:
				print("Letter not in the word. Hangman status: ")
				print(hangman[hangman_status])
				hangman_status += 1
				
		elif player_guess_letter in provided_letters:
			print("You already used this letter. Try a different one.")
		#	return player_letter()
		elif player_guess_letter not in letters:
			print("This is not a valid letter. Please try again.")
		#	return player_letter

	if hangman_status == 11:
		print("You lost!")
	else:
		print("You won! You guessed that the word is: ", ''.join(word))

	play_again()


def play_again():
	new_game = input("Do you want to play again?: ").upper()
	if new_game == "Y":
		return hangman()
	else:
		print("Thanks for playing!")


hangman()
#play_again()


