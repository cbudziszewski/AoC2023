#!/usr/bin/env python3

import re

sum = 0;

# aparently you have to match "oneight" as 18 ...
translate = {
        "on":"1",
        "tw":"2",
        "thre":"3",
        "fou":"4",
        "fiv":"5",
        "si":"6",
        "seve":"7",
        "eigh":"8",
        "nin":"9",
        "zer":"0",
        }

regex = re.compile('on(?=e)|tw(?=o)|thre(?=e)|fou(?=r)|fiv(?=e)|si(?=x)|seve(?=n)|eigh(?=t)|nin(?=e)|zer(?=o)')

with open('input') as f:
    for line in f:
        modline = regex.sub(lambda m: translate[m.group(0)] , line)
        numbers = re.findall(r'\d', modline)
        sum += int(numbers[0] + "" + numbers[-1])

print(f"Result: {sum}")

