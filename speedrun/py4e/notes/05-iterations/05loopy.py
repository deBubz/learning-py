# 05 Loops

# method a
# takes in a sequence of numbers, return the average when user input x
def methodA():
    total = 0
    count = 0
    while True:
        notX = input("$ ")
        if notX == 'x':                                 # end program
            if count == 0:  break                       # stop dividing by 0
            else:   print(float(total)/float(count))    # output average
        else:
            try:
                total = total + int(notX)
                count = count + 1
            except: print("Bad Input")

    print("Game Ended")

# method b
# takes in a sequence of numbers
def methodB():
    notX = input('! ')
    first = True
    max = 0
    min = 0
    
    while notX != 'x':
        try:
            if first:       # inital input
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

# Basicly the same as methodb
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


print("05 loops\n")
print("3 methods")
print("\tmethodA grabs a sequence of number and returns an average when end")
print("\tmethoB C returns the min an max number of the sequence")
print("using B to demo but have a look and spot the difference")

def run_prompt():
    print()
    print("1. A get average")
    print("2. B, C get minmax")
    print()
    return input("pick your choice: ")

def run():
    while True:
        a = run_prompt()
        if a == 'x':
            print("======================")
            print("Closing")
            print("======================")
            exit()
        elif a == '1':
            methodA()
        elif a == '2':
            methodB()
        else:
            print("======================")
            print("Invalid input")
        print("======================")

    
run()
