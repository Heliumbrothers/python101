import os
os.system('cls' if os.name == 'sts' else 'clear') 
bids = {}

print('Welcome to the Silent Auction')
name = input('What is your name: ')
amount_bid = float(input('How much are you going to bid: £'))
print('Thank you!')
bids[name] = amount_bid
cont = (input('Are there any other people that want to bid? Type \'yes\' for yes and \'no\' for no: ')).lower()
while cont == 'yes':
    os.system('cls' if os.name == 'sts' else 'clear')
    print('Welcome to the Silent Auction')
    name = input('What is your name:')
    amount_bid = input('How much are you going to bid: £')
    print('Thank you!')
    cont = input('Are there any other people that want to bid? Type \'yes\' for yes and \'no\' for no: ').lower()


highest_bid = 0
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]

highest_bidder = (list(bids.keys())
      [list(bids.values()).index(highest_bid)])

print(f'{highest_bidder} wins, with a bid of £{highest_bid}')