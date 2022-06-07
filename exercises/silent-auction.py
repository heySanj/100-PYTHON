import os
clear = lambda: os.system('clear')
clear()

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

highest_bid = 0
highest_bidder = ""
bids = {}

while True:
    print(logo)
    print("\nWelcome to the Secret Auction Program.")
    
    new_bidder = input("\nWhat is your name?: ")
    new_bid = int(input("\nWhat is your bid? $"))

    bids[new_bidder] = new_bid

    repeat = input("\nWould someone else like to bid? 'y' or 'n': ")
    
    if repeat == "n":
        break
    else:
        clear()


# Find the highest bidder
for bid in bids:
    # print(f"{bid} bids ${bids[bid]}")
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        highest_bidder = bid

clear()
print(logo)
print("\nWelcome to the Secret Auction Program.")        
print(f"\n{highest_bidder} has won the auction with a bid of ${highest_bid}!\n\n")