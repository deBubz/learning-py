# 02 variables exercises

# # input name and print
def nameInput():
    name = input("Enter your name: ")
    print("Hello %s" % name)

# # Enter hour+rate and print earnings
def grossPay():
    hrs = input("Enter hours: ")
    rate = input("Enter rate: ")
    print("Pay: %s" % (
        round((float(rate) * float(hrs)), 2)
        ))

def expressions():
    width = 17
    height = 12.0

    print(width//2)
    print(width/2.0)
    print(height/3)

def celcToFarens():
    celc = float(input("Temp in C: "))
    print("Temp in F: %s" % ((celc * 1.8) +32))

# # # Run everything
# while(input("Please pick one") != 'x'):
#     print("letsgo")

nameInput()
grossPay()
expressions()
celcToFarens()
