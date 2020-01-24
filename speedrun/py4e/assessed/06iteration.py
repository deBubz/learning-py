# infinite input program

# method a
def inputMe():
    total = 0
    count = 0
    while True:
        notX = input("$ ")
        if notX == 'x':
            if count == 0:  break
            else:   print(float(total)/float(count))
        else:
            try:
                total = total + int(notX)
                count = count + 1
            except: print("Bad Input")

    print("Game Ended")

# method b
def anotherInput():
    notX = input('! ')
    max = 0
    min = 0
    first = True
    
    while notX != 'x':
        try:
            if first:
                max = int(notX)
                min = int(notX)
                first = False
            else:
                if max < int(notX): max = int(notX)
                if min > int(notX): min = int(notX)
        except: print("bad input")
        notX = input('! ')

    if first == False:
        print("Max", max)
        print("Min", min)

def methodC():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            if largest == None or largest < int(num):
                largest = int(num)
            if smallest == None or smallest > int(num):
                smallest = int(num)
        except:
            print("bad input")
            
    print("Maximum is", largest)
    print("Minimum is", smallest)

methodC()