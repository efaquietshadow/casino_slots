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

print("Welcome to the _blank_ slot machine")
print("You have __ in your wallet")
print("Would you like to play? Y/N  ")
play_again = input()

wallet_amount = ("$")
starting_wallet = ("$" + 1000)

# if statement to check if input equeals Y or N
if play_again == "Y":
    print("What would you like to bet?")
    current_bet = input("$")

if play_again == "N":
    print("We hope to see you again")