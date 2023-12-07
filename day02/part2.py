#!/usr/bin/env python3

import re
from functools import reduce

sum = 0;

max_dice={'red':12, 'green':13, 'blue':14 }

game_re = re.compile('Game (?P<game>\d+):')
color_re = re.compile('(\d+) (\w+)')

print(game_re)
print(color_re)

with open('input') as f:
    for line in f:
        # Game xx: group1 ; group2; group3 ...
        game = game_re.match(line)
        game_possible = True;
        min_dice = {k:0 for k in max_dice.keys()}
        for draws in line.split(':')[1:]:
            for d in draws.split(';'):
                counts = color_re.findall(d)
                for c, k in counts:
                    min_dice[k] = max(min_dice[k], int(c))
        pwr = reduce(lambda r, v: r * v, min_dice.values(), 1)
        print(f"Game {int(game.group('game'))} is possible with : {min_dice} , power is {pwr} ")
        sum += pwr
        

print(f"Result: {sum}")

