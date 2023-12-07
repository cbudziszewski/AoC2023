#!/usr/bin/env python3

import re

from functools import reduce
import operator

with open('input') as f:
    for line in f:
        if line.startswith('Time'):
            times = list(map(int,re.findall(r'\d+',line)))
        if line.startswith('Dist'):
            distances = list(map(int,re.findall(r'\d+',line)))

print(f"times: {times}")
print(f"dist: {distances}")


def travel_distance(charge_time,race_duration):
    speed = charge_time
    travel_time = race_duration - charge_time
    return travel_time * speed

winning_charge_times = list()

for race, raceduration in enumerate(times):
    winning_charge_times.append(sum([ travel_distance(ct,raceduration)>distances[race] for ct in range(0,raceduration)]))

print(reduce(operator.mul,winning_charge_times,1))

