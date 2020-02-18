# global file select
fname = None
fh = None

def open_file():
    try:
        # string = "../data/" + input("File Nale: ")
        string = "mbox-short.txt"
        handler = open("mbox-short.txt")
        print("Succesfuly oppened", string)
        return handler
    except:
        print("Unable to read", string)
        exit()
    


# ex 1
# read and prints file content in uppercase
def e1_toupper():
    line = 0
    for l in fh:
        if line == 10: break
        print(l.upper())
        line = line + 1



# ex 2
# Use the file name mbox-short.txt as the file name
def ex2_counting_avg():
    total = float(0)
    count = 0

    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"): continue
        else:
            count = count + 1
            total = total + float(line[20:])

    # do average
    print("Average spam confidence: %s" % (float(total)/ count))
    print()



# ex 3
# ask to input data name, add easter egg
def e3_easter_egg():
    file_name = input("Enter a file name: ")
    if file_name == "this is lame":
        print("BAMBOOZLED")
        exit()

    count = 0
    for l in fh:
        count = count + 1

    print(count)



################################
##      Do the Program        ##
################################

def run_prompt():
    print("07 files ex")
    print()
    print("1. string name")
    print("2. gross pay calc")
    print("3. random expressions")
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
        elif a == '2': ex2_counting_avg()
        # elif a == '3': e4_expressions()
        elif a == 'c': open_file()
        else:
            print("======================")
            print("Invalid input\n")

fh = open_file() 
run()
