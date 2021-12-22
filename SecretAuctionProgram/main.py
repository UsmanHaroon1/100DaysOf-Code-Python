from art import logo
import os

print(logo)
print("Welcome to secret auction program")

bidding_finished = False

bid_dict = {}
while not bidding_finished:
    os.system('cls')
    user = input('what is your name?')
    amount = int(input('what is your bid?$'))

    bid_dict[user] = amount

    choice = input('Type "yes" to enter another user, Type "no" to end this bid').lower()
    if(choice == "no"):
        bidding_finished = True

winner = ""
winning_price = 0
for key in bid_dict:
    if bid_dict[key] > winning_price:
        winner = key
        winning_price = bid_dict[key]

print(f"The winner is {winner} with the bid of ${winning_price}")
