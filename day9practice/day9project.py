import os
import math

print("Welcome to the secret auction program.")

running = True
bidders = []


def bidding_program():

    new_bidder = {
        "name": name,
        "bid": bid,
    }

    bidders.append(new_bidder)


while running == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if others == "no":
        running = False
        bidding_program()
    elif others == "yes":
        os.system('clear')
        bidding_program()
    

def print_bidders(bidders):
    for bidder in bidders:
        print(f"The bidder: '{bidder['name']}', bid: ${bidder['bid']}")
        
def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ""

    for bidder in bidders:
        if bidder['bid'] > highest_bid:
            highest_bid = bidder['bid']
            highest_bidder = bidder['name']
    print(f"The highest bidder was:{highest_bidder} with a ${highest_bid} bid!")

print_bidders(bidders)
find_highest_bidder(bidders)


