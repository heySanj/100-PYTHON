import random
import os
clear = lambda: os.system('clear')
clear()

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
    
def deal():
    draw_card(player_hand, 2)    
    draw_card(dealer_hand, 2)
    
        
def draw_card(hand, amount):
    while amount > 0:
        hand.append(random.choice(cards))
        amount -= 1
        
def dealer_play():
    while sum(dealer_hand) < 17:
        draw_card(dealer_hand, 1)
        ace(dealer_hand)
    print(f"\n\tYour final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"\tComputer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
    
    # Determine and print winner
    print(winner())
    
    # Ask to play again
    play_game()
        
def print_hands():
    print(f"\n\tYour cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"\tComputer's first card: {dealer_hand[0]}")
    
def ask_player():
    while sum(player_hand) < 21:
        player_draw = input("\nType 'y' to get another card, type 'n' to pass: ")

        if player_draw == 'y':
            draw_card(player_hand, 1)
            ace(player_hand)
            print_hands()
        else:
            break
            
    dealer_play()

# Change 11 to 1 if you go bust            
def ace(hand):
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
            

def winner():
    
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    
    if player_score == dealer_score:
        return "\nDraw... 🙃\n"
    elif dealer_score == 21 and len(dealer_hand) == 2:
        return "\nLose, opponent has Blackjack! 😱\n"
    elif player_score == 21 and len(player_hand) == 2:
        return "\nWin with a Blackjack! 😎\n"
    elif player_score > 21:
        return "\nYou went over. You lose! 😭\n"
    elif player_score > 21:
        return "\nOpponent went over. You win! 😁\n"
    elif player_score > dealer_score:
        return "\nYou win! 😃\n"
    else:
        return "\nYou lose... 😤\n"
    
def play_game():
    player_hand.clear()
    dealer_hand.clear()
    
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        clear()
        print(logo)
        deal()
        print_hands()
        ask_player()
    else:
        exit()
        
play_game()
    
