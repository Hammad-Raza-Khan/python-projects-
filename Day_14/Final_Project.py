from one import logo, vs
from two import data
import random
from replit import clear # type: ignore

score = 0
entity_b = random.choice(data)

while True:
    entity_a = entity_b
    entity_b = random.choice(data)
    while entity_a == entity_b:
        entity_b = random.choice(data)


    name = entity_a["name"]
    follower_count = entity_a["follower_count"]
    description = entity_a["description"]
    country = entity_a["country"]

    name_b = entity_b["name"]
    follower_count_b = entity_b["follower_count"]
    description_b = entity_b["description"]
    country_b = entity_b["country"]



    print(logo)
    print(f"Compare A: {name}, {description}, from {country}")
    print(vs)
    print(f"Compare B: {name_b}, {description_b}, from {country_b}")

    user_guess = input("Who Has More Followers? \n A or B ? \n:").upper()

    def check_guess(user_guess, follower_count, follower_count_b):
        if follower_count > follower_count_b:
            return user_guess == "A"
        else:
            return user_guess == "B"

    is_correct = check_guess(user_guess, follower_count, follower_count_b)

    clear()
    
    if is_correct == True:
        score+=1
        print(f"You Got it Right ! Your current score is {score }")
    else:
        print(f"Sorry! You Got it Wrong ! Your score is {score }")
        break



