# 03 conditionals excercises

## for ex 1
class Pay:
    def __init__(self):
        self.ot_flag = False
        self.rate = 0.0
        self.hours = 0.0
        self.ot_rate = 0.0
        self.ot_hours = 0.0

    # Get input
    def getData(self):      
        try:
            self.rate = float(input("Enter Pay: "))
            self.hours = float(input("Enter Hours: "))

            if self.hours > 40:
                self.ot_flag = True
                self.ot_rate = self.rate * 1.5
                self.ot_hours = self.hours - 40
        except:
            print("please enter a valid number")

    # prints output
    def getPay(self):
        if self.ot_flag is False:
            print("Pay: %s" % (self.rate * self.hours))
        else:
            print("Gross Pay: %s" % ((self.rate * self.hours) + (self.ot_pay * self.ot_hours)))




# # gross pay calculation ex using the defined class above
def e1_payme():
    payme = Pay()

    payme.getData()
    payme.getPay()

# # Ex 3 if else exercise
def e3_grading():
    try:
        sx = input("Enter Score(0.0 - 1.0): ")
        score = float(sx)
        msg = ''

        if score <= 1.0 and score >= 0.9:
	        msg = "A"
        elif score < 0.9:
	        msg = "B"
        elif score < 0.8:
	        msg = "C"
        elif score < 0.7:
	        msg = "D"
        elif score >= 0 and score < 0.6:
	        msg = "F"
        else:
	        msg = "error"
    
        print("You got a", msg)
    except:
        print("Input error")


################################
##      Do the Program        ##
################################

def run_prompt():
    print("03 conditionals ex")
    print()
    print("1. Pay calc")
    print("3. Grading program")
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
            e1_payme()
        elif a == '3':
            e3_grading()
        else:
            print("======================")
            print("Invalid input")
        print("======================")

    
run()

