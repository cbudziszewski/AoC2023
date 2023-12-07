#!/usr/bin/env python3

import re

sum = 0;

max_dice={'red':12, 'green':13, 'blue':14 }

game_re = re.compile('Game (?P<game>\d+):')
#color_re = re.compile('|'.join(map(lambda s: f".(?P<{s}>\d+) {s}", max_dice.keys())))
color_re = re.compile('(\d+) (\w+)')

print(game_re)
print(color_re)

with open('input') as f:
    for line in f:
        # Game xx: group1 ; group2; group3 ...
        game = game_re.match(line)
        game_possible = True;
        for draws in line.split(':')[1:]:
            for d in draws.split(';'):
                counts = color_re.findall(d)
                game_possible &= all([int(c) <= max_dice[k] for c, k in counts])

        print(f"Game {int(game.group('game'))} is possible: {game_possible}")
        if game_possible:
            sum += int(game.group('game'))
        

print(f"Result: {sum}")

