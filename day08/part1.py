#!/usr/bin/env python3

import re

instructions=list()
network=dict()

with open('input') as f:
    for line in f:
        if '=' in line:
            groups = re.match(r'(\b\w+).=..(\b\w+), (\b\w+).',line).groups()
            network[groups[0]]=dict()
            network[groups[0]]['L']=groups[1]
            network[groups[0]]['R']=groups[2]

        else:
            instructions.extend(re.findall(r'\w',line))

print(network)
print(instructions)

position='AAA'

stepcount = 0
move = 0
while position != 'ZZZ':
    position = network[position][instructions[move]]
    stepcount += 1
    move = (move + 1) % len(instructions)

print(f'took {stepcount} steps to reach "ZZZ" with {"".join(instructions)}')



