#!/usr/bin/env python3

import re

from CamelCards import Hand

list_of_hands = list()
with open('input') as f:
    for line in f:
        m = re.match(r'(\b\w+) (\b\d+)', line).groups()
        list_of_hands.append(Hand(m[0], int(m[1]), joker=True))

#for hand in list_of_hands:
#    print(f"{hand} {hand.handtype()}")

sort_fun = lambda hand: hand.as_number() 
sorted_list_of_hands = sorted(list_of_hands, key=lambda hand: hand.as_number())

sum = 0
for rank, hand in enumerate(sorted_list_of_hands,1):
    print(f"rank {rank}, card {hand.cards} {hand.handtype()}")
    sum = sum + (rank * hand.bid)

print(f"total Winnings: {sum}")

