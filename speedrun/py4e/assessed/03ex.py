def overtime():
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

def grading():
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