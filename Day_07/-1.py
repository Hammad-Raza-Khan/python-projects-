#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
choosen_word = random.choice(word_list)
print(choosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter to save THE HANGMAN ! \n").lower()
print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for every_letter in choosen_word:
    if every_letter == guess:
        print("right")
    else:
        print("wrong")
    
