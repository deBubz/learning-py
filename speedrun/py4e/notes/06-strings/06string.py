# 07 Strings

# e1 traverse and print each char backwards
def e1_backwards():
    back = input("enter a string: ")
    index = len(back) - 1

    while index >= 0:
        print(back[index])
        index = index - 1

# count the occurance of letter a in a string
def e3_counting_a(a):
    word = a
    count = 0

    for let in word:
        if let == 'a': count = count + 1

    print(count)

def e4_better_count():
    try:
        word = input("Enter the string: ")
        match = input("what you want to count: ")

        if(len(match) != 1): print("input error")

        print(word.count(match))
    except:
        print("input error")


# prints out the number
def e5_parsing():
    text = "X-DSPAM-Confidence:    0.8475"

    i = text.find("0")
    x = float(text[i:])             # splice from char 0
    print(x)
    print("better off reading the code for this\n")

################################
##      Do the Program        ##
################################

def run_prompt():
    print("\n010 strings")
    print()
    print("1. reverse string")
    print("3. count a")
    print("4. count char in word")
    print("5. parsing ex")
    print()
    return input("pick your choice: ")

def close_prompt():
    print("======================")
    print("Closing\n")
    exit()

def run():
    while True:
        a = run_prompt()
        if a == 'x':    close_prompt()
        elif a == '1':  e1_backwards()
        elif a == '3':  e3_counting_a(input("Enter a string: "))
        elif a == '4':  e4_better_count()
        elif a == '5':  e5_parsing()
        else:
            print("======================")
            print("Invalid input\n")

    
run()