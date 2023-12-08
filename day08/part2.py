#!/usr/bin/env python3

import re

from math import lcm

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

def solve(start, instructions, network):
    steps = 0
    pos = start
    while pos[2] != 'Z':
        pos = network[pos][instructions[steps%len(instructions)]]
        steps +=1
    print(f"starting position {start} ends at {pos} after {steps} steps")
    print(f"{network[start]} - {network[pos]} : remaining instr = {steps%len(instructions)}")
    return steps

start = [k for k in network.keys() if k[2] == 'A']
stop  = [k for k in network.keys() if k[2] == 'Z']

print(f"starting at {start}")

ghost_steps = [ solve(pos, instructions, network) for pos in start ]

print(f"we now realize, we fully cycle all instructions in each case, with no left over.")
print(f"start and stop positions are bijective and following stop positions, lead you on the same cycle again.")
print(f"finding the 'kgt' (or lcm) is the way to go...")
print(f"solution: { lcm(*ghost_steps) }")

exit()

# brute force way: 
stepcount = 0
move = 0
while any([e[2] != 'Z' for e in positions]):
    turn = instructions[move]
    positions = [ network[p][turn] for p in positions ]
    stepcount += 1
    move = (move + 1) % len(instructions)

print(f'took {stepcount} steps to reach every "..Z" with {"".join(instructions)}')

