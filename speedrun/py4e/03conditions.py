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