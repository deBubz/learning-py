# 02 variables exercises

# # input name and print
def e2_nameInput():
    name = input("Enter your name: ")
    print("Hello %s" % name)
    print()

# # Enter hour+rate and print earnings
def e3_grossPay():
    hrs = input("Enter hours: ")
    rate = input("Enter rate: ")
    print("Pay: %s" % (
        round((float(rate) * float(hrs)), 2)
        ))
    print()

# print out various expressions
def e4_expressions():
    width = 17
    height = 12.0

    print(width//2)
    print(width/2.0)
    print(height/3)
    print()

# convert celcius to fahrenheit
def e5_celcToFarens():
    celc = float(input("Temp in C: "))
    print("Temp in F: %s" % ((celc * 1.8) +32))
    print()

################################
##      Do the Program        ##
################################

def run_prompt():
    print("02 variables ex")
    print()
    print("2. string name")
    print("3. gross pay calc")
    print("4. random expressions")
    print("5. C to F")
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
        if a == 'x':
            close_prompt()
        elif a == '2':
            e2_nameInput()
        elif a == '3':
            e3_grossPay()
        elif a == '4':
            e4_expressions()
        elif a == '5':
            e5_celcToFarens()
        else:
            print("======================")
            print("Invalid input\n")

    
run()
