#!/usr/bin/env python3

import re

sum = 0;

pile_of_todo = list()
pile_of_reference = dict()


with open('input') as f:
    for line in f:
        line_split = re.split(r':|\||\n', line)
        card = re.search(r'\d+', line_split[0]).group(0)
        winning = list(map(int,re.findall(r'\d+', line_split[1])))
        numbers = list(map(int,re.findall(r'\d+', line_split[2])))
        intersect = list(set(winning) & set(numbers))
        wins =  len(intersect)

        pile_of_reference[int(card)] = wins
        pile_of_todo.append(int(card))

        

while len(pile_of_todo)>0:
    # print(pile_of_todo)
    card = pile_of_todo.pop()
    sum += 1
    for copy in range(card + 1, card + pile_of_reference[card] + 1):
#        print(f"card {card} appends {copy}")
        pile_of_todo.append(copy)



print(f"Result: {sum}")

