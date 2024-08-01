art = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
        
        """
 
print(art)
EASY_ATTEMPTS = 10
HARD_LEVEL_TURNS = 5
from random import randint
random_number = randint(1,100)

def check_answer(guess, random_number, turns):
      if guess > random_number:
        print("Try Low !")
        return turns - 1
        # print(f"Attempts left : {attempts}")
        # a = int(input("Guess the number: "))
      elif guess < random_number:
        print("Try High !")
        return turns - 1
        #a = int(input("Guess the number: "))
      else :
        print(f"You Got it ! The answer was {random_number}")
        
        
def welcome():
    choose = input("Choose a level: easy or hard: ")
    if choose == 'easy':
       return EASY_ATTEMPTS
        
    elif choose == 'hard':
        return HARD_LEVEL_TURNS

def guessing():
    print("Welcome to the Number Guessing Game!")
    print("A number between 1 and 100.")
    print(f"Pssst, the correct answer is {random_number}") 
    
    turns = welcome()
    guess = 0
    while guess != random_number:
      print(f"You have {turns} attempts remaining to guess the number.")

      guess = int(input("Guess the number: "))
    
      turns = check_answer(guess, random_number, turns)
      if turns == 0:
        print("You've run out of guesses, you lose.")
        return
      elif guess != random_number:
        print("Guess again.")
  

guessing()