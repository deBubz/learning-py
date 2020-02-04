# regex assessment

import re

f_name = '../data/regex_sum_354193.txt'
hand = open(f_name)
total = 0

for line in hand:
   line.strip()
   x = re.findall('[0-9]+', line)
   if len(x) > 0:
       for num in x:
           total = total + int(num)

print(total)

# Try the just for fun one??