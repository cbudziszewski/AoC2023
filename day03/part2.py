#!/usr/bin/env python3

import re

sum = 0;

number_re = re.compile(r'\d+')
part_re = re.compile(r'[^0-9\.\n]')

the_numbers = list()
the_symbols = list()

with open('input') as f:
    for count, line in enumerate(f):
        the_numbers.extend([(count, m.start(), m.end()-1, int(m.group(0))) for m in number_re.finditer(line)])
        the_symbols.extend([(count, m.start(), m.group(0)) for m in part_re.finditer(line)])

print(the_numbers)
print(the_symbols)

gears = [ g for g in the_symbols if g[2] == '*']

print(f"gears: {gears}")

for sn in the_symbols:
  # check if symbol is a gear.
  
  count = [ pn[3] for pn in the_numbers if (sn[0] >= pn[0]-1) and (sn[0] <= pn[0]+1) and  (sn[1] >= pn[1]-1) and (sn[1] <= pn[2]+1)]

  if len(count)==2:
      print(f"{sn} is a gear with ratio {count[0]} * {count[1]} = {count[0] * count[1]}")
      sum += count[0]*count[1]
  else:
      print(f"{sn} is not a gear")


print(f"Result: {sum}")

