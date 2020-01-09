intput = [
    3, 5, 2, 1, 0 , 9 , 11, 12, 7 ,8, 8, 8
]

counter = 0

for x in range(0, len(intput)):
    for y in range(1, len(intput) - x):
        if intput[y] > intput[y-1]:
            temp = intput[y]
            intput[y] = intput[y-1]
            intput[y-1] = temp

            counter = counter + 1
            print("%s. %s" % (counter ,intput))
   