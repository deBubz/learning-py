# NOTE: bug when trying to run e2 twice
# Handler needs to be resetted
# handler reached the end of file
# therefore when ran again, it starts itterating from the end

# global file select
fh = None

def open_file(f_name):
    if f_name == "notnow":
        print("get bamboozled")
        exit()
    try:
        handler = open(f_name)
        print("Successfully opened", f_name)
        return handler
    except:
        print("Unable to read", f_name)
        print("Enter one of these:\nmbox.txt\nmbox-short.txt")
        exit()

# ex 1
# read and prints file content in uppercase
def e1_toupper():
    try:
        limit = int(input("Uppercase how many lines "))
        line = 0

        for l in fh:
            if line == limit: break
            print(l.upper())
            line = line + 1
    except:
        print("Please enter a number")
        exit()

# ex 2
# Use the file name mbox-short.txt as the file name
def e2_counting_avg():
    total = float(0)
    count = 0
    print(total, count)
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"): continue
        else:
            count = count + 1
            total = total + float(line[20:])

    # do average
    if count == 0:
        print("Not present in file")
        exit()
    print("Average spam confidence: %s" % (float(total)/ count))
    print()

################################
##      Do the Program        ##
################################

def run_prompt():
    print("07 files ex")
    print()
    print("1. string name")
    print("2. avg of something")
    print("c. change selected file")
    print()
    return input("pick your choice: ")

def close_prompt():
    print("======================")
    print("Closing")
    print("======================")
    exit()

def run():
    while True:
        a = run_prompt()
        if a == 'x': close_prompt()
        elif a == '1': e1_toupper()
        elif a == '2': e2_counting_avg()
        # elif a == '3': e4_expressions()
        elif a == 'c': open_file(input("Enter File Name: "))
        else:
            print("======================")
            print("Invalid input\n")

fh = open_file("mbox-short.txt") 
run()
