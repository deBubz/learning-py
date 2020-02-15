# Use the file name mbox-short.txt as the file name
total = float(0)
count = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    else:
        count = count + 1
        total = total + float(line[20:])

# do average
print("Average spam confidence: %s" % (float(total)/ count))