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

for pn in the_numbers:
  # check if number is a part number.
  # the number needs to touch a symbol on its perimeter box.
  
  hit = any([ (sn[0] >= pn[0]-1) and (sn[0] <= pn[0]+1) and  (sn[1] >= pn[1]-1) and (sn[1] <= pn[2]+1) for sn in the_symbols])

  if hit:
      print(f"{pn} is a part number")
      sum += pn[3]
  else:
      print(f"{pn} is not a part number")


print(f"Result: {sum}")

