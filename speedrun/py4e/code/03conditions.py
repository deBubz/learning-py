# rewrite gross pay to include overtime
# rewrite gross pay to include exeption handling

class Pay:
    def __init__(self):
        self.ot_flag = False
        self.rate = 0.0
        self.hours = 0.0
        self.ot_rate = 0.0
        self.ot_hours = 0.0

    def getData(self):
        try:
            self.rate = float(input("Enter Pay: "))
            self.hours = float(input("Enter Hours: "))

            if hours > 40:
                self.ot_flag = True
                self.ot_rate = self.rate * 1.5
                self.ot_hours = self.hours - 40
        except:
            print("please enter a valid number")

    def getPay(self):
        if self.ot_flag is False:
            print("Pay: %s" % (self.rate * self.hours))
        else:
            print("Gross Pay: %s" % ((self.rate * self.hours) + (self.ot_pay * self.ot_hours)))

steve = Pay()
steve.getData()
steve.getPay()

########### IDK what this is

hrs = float(input("Enter Hours:"))
pay = float(input("Enter rate:"))


def paying(hours, pay):
    return (hours * pay)

if hrs > 40:
    ot_pay = pay*1.5
    ot_hrs = hrs - 40
    total = paying(40, pay) + paying(ot_hrs, ot_pay)
    print(total)
else:
    print(paying(hrs, pay))

# seems the same as above
#############

sx = input("Enter Score: ")
score = float(sx)
msg = ''

if score <= 1.0 and score >= 0.9:
	msg = "A"
elif score >= 0.8:
	msg = "B"
elif score >= 0.7:
	msg = "C"
elif score >= 0.6:
	msg = "D"
elif score >= 0 and score < 0.6:
	msg = "F"
else:
	msg = "error"
    
print(msg)
