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


def roll_slots(): 
    slot_options = ("| Unicorn |", "| Dragon |", "| Sword |", "| Gold |", "| Castle |", "| Knight |")
    roll_one = random.choice(slot_options)
    roll_two = random.choice(slot_options)
    roll_three = random.choice(slot_options)
    print(roll_one, roll_two, roll_three)

    global current_bet
    global wallet_amount


    if roll_one == roll_two == roll_three:
        current_bet *= 3
        wallet_amount += current_bet
        print(f"You won ${current_bet}!")


    elif roll_one == roll_two:
        current_bet *= 2
        wallet_amount += current_bet
        print(f"You won ${current_bet}!")
    
    elif roll_one == roll_three:
        current_bet *= 2
        wallet_amount += current_bet
        print(f"You won ${current_bet}!")

    elif roll_three == roll_two:
        current_bet *= 2
        wallet_amount += current_bet
        print(f"You won ${current_bet}!")

    else:
        print("Sorry you lost, want to try again?")


print("Welcome to the _blank_ slot machine")

# tofix so i can have $ and a number
wallet_amount = 1000
current_bet = 0

while wallet_amount > 0:
    print(f"You have ${wallet_amount} in your wallet")
    print("Would you like to play again? Y/N  ")
    play_again = input()
    # if statement to check if input equeals Y or N
    if play_again.upper() == "Y":
        print("What would you like to bet?")
        bet_input = input()
        current_bet = int(bet_input)
        wallet_amount -= current_bet
        roll_slots()

    if play_again.upper() == "N":
        print("We hope to see you again")
        break

if wallet_amount <= 0:
    print("You ran out of money, come back again later")


# The options it randomly chooses between


# see if i can figure out how to make a table later
