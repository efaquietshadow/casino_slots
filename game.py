# Welcome message
# show wallet
# Ask if they want to play
# Set a random jackpot?
# Roll random choice of items
# Items being a fantasy style theme?
# Check if any match
# matching equals winning, different amounts maybe? 
# Two matches is different than three matches
# Comment on if you won or lost
# Show amount you won if any
# Show current wallet and ask if they want to play again.

import random

print("Welcome to the _blank_ slot machine")
print("You have $1000 in your wallet")
print("Would you like to play? Y/N  ")
play_again = input()

# tofix so i can have $ and a number
wallet_amount = ()

def roll_slots(): 
    slot_options = ("| Unicorn |", "| Dragon |", "| Sword |", "| Gold |", "| Castle |", "| Knight |")
    print(random.choice(slot_options), random.choice(slot_options), random.choice(slot_options))


# if statement to check if input equeals Y or N
if play_again.upper() == "Y":
    print("What would you like to bet?")
    current_bet = input("$")
    roll_slots()

if play_again.upper() == "N":
    print("We hope to see you again")


# The options it randomly chooses between


# see if i can figure out how to make a table later
