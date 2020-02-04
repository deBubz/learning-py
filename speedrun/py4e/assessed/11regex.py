# regex assessment

import re
import os

f_name = '../data/regex_sum_42.txt'
print("opening", f_name)
hand = open(f_name)

for line in hand:
    print(line)