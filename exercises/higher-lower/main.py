from game_data import data
import random
from art import logo, vs

import os
clear = lambda: os.system('clear')
clear()




# Generate a random account from the game data.
def get_rand_account():
    return random.choice(data)

# Format account data into printable format.
def format_account(data):
    # return f"{data['name']}, a {data['description']}, from {data['country']}, followers: {data['follower_count']}"
    return f"{data['name']}, a {data['description']}, from {data['country']}"

def lose():
    clear()
    print(logo)
    print(f"Sorry, thats wrong. Final Score: {score}.")
    quit()


score = 0
account_a = get_rand_account()
account_b = get_rand_account()

# game.
while True:
    clear()
    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")
        
    
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")

    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer == 'a' and a_followers >= b_followers:        
        score += 1
        account_a = account_b
        account_b = get_rand_account()        
    elif answer == 'b' and b_followers >= a_followers:
        score += 1
        account_a = account_b
        account_b = get_rand_account()
    else:
        lose()




