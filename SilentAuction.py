import os

dict_2 = {}

def add_bidder(name, bid):
    dict_1 = {}
    dict_1[name] = bid
    dict_2.update(dict_1)

other_bidders = 'yes'
while other_bidders != 'no':
    bidder_name = input("What is your name?")
    bid_amount = int(input("What is your bid?"))
    add_bidder(bidder_name, bid_amount)
    other_bidders = input("Are there any other bidders?")
    if other_bidders == 'yes':
        os.system('cls')
    if other_bidders == 'no':
        break

z = 0
for i, j in dict_2.items():
    j = int(dict_2[bidder_name])
    if j > z:
        z = j
        winner_name = i

print(f"the winner is {winner_name} with a bid of {z}")
