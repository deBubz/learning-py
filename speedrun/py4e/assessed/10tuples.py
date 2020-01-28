# Basicly exercise 10.2
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counting = dict()


for line in handle:
    line.strip()
    if line.startswith("From "):
        value = line.split()[5].split(':')[0]			# parsing
        counting[value] = counting.get(value, 0) + 1

# decorate
lst = list()	# list tuple
for key in counting:
    lst.append((key, counting[key]))
# sort
lst.sort()
# undecorate
for k, v in lst:
    print(k, v)
    
