# 02 variables exercises

# # input name and print
def e1_nameInput():
    name = input("Enter your name: ")
    print("Hello %s" % name)
    print()

# # Enter hour+rate and print earnings
def e2_grossPay():
    hrs = input("Enter hours: ")
    rate = input("Enter rate: ")
    print("Pay: %s" % (
        round((float(rate) * float(hrs)), 2)
        ))
    print()

def e3_expressions():
    width = 17
    height = 12.0

    print(width//2)
    print(width/2.0)
    print(height/3)
    print()

def e4_celcToFarens():
    celc = float(input("Temp in C: "))
    print("Temp in F: %s" % ((celc * 1.8) +32))
    print()

################################
##      Do the Program        ##
################################

def run_prompt():
    print("03 variables ex")
    print()
    print("1. string name")
    print("2. gross pay calc")
    print("4. C to F")
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
            e1_nameInput()
        elif a == '2':
            e2_grossPay()
        elif a == '3':
            e4_celcToFarens()
        else:
            print("======================")
            print("Invalid input")
        print("======================")

    
run()
