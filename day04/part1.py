#!/usr/bin/env python3

import re

sum = 0;


with open('input') as f:
    for line in f:
        line_parts = re.split(r':|\||\n',line)
        game = re.match(r'\d+',line_parts[0])
        winning = list(map(int,re.findall(r'\d+', line_parts[1])))
        numbers = list(map(int,re.findall(r'\d+', line_parts[2])))

        intersect = list(set(winning) & set(numbers))
        points =  pow(2,len(intersect)-1) if len(intersect)>0 else 0

        print(f"points {points}")

        sum += points
        


print(f"Result: {sum}")

