# fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
# print(line.rstrip())
