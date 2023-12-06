#!/usr/bin/env python3

import re

sum = 0;

with open('input') as f:
    for line in f:
        numbers = re.findall(r'\d', line)
        sum += int(numbers[0] + "" + numbers[-1])

print(f"Result: {sum}")

