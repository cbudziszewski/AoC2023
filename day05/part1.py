#!/usr/bin/env python3

import re

almanac = dict()

with open('input') as f:
    for line in f:
        if ':' in line:
            key = re.match(r'^[\w-]+',line).group(0)
            if key == 'seeds':
                seeds = list(map(int,re.findall(r'\d+',line)))
                print(f"seeds {seeds}")
            else:
                almanac[key] = list()
        else:
            row = tuple(map(int,re.findall(r'\d+',line)))
            if len(row) > 0:
                almanac[key].append(row)
#        print(almanac)

def lookup(mapsrc,mapdest, item):
    key = mapsrc + '-to-' + mapdest
    for row in almanac[key]:
        if item >= row[1] and item <= row[1]+row[2]:
            offset = item - row[1]
#            print(f"found {item} in {row}. offset {offset} < {row[2]}")
            return row[0] + offset
#    print(f'default return {item}')
    return(item)

loclist = list()
for s in seeds:
    soil        = lookup('seed','soil',s)
    fertilizer  = lookup('soil','fertilizer', soil)
    water       = lookup('fertilizer','water', fertilizer)
    light       = lookup('water','light', water)
    temperature = lookup('light','temperature', light)
    humidity    = lookup('temperature','humidity', temperature) 
    location    = lookup('humidity','location', humidity)
    print(f'seed {s}, soil {soil}. fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}')
    loclist.append(location)

result = min(loclist)
print(f'the lowest number for any initial seed is {result}')
    

