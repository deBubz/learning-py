import sys

# testing using inputs
def agePrint(age, ageString):
    print("%s?, %s" % (age, ageString))

def ageCheck(age):
    if age < 15:
        agePrint(age, "yer a loli")
    elif age > 30:
        agePrint(age, "yer a pedo")
    else:
        agePrint(age, "what are you")


# print("How old are you?")
ageCheck(int(input("How old are you?")))
# ageCheck(int(sys.stdin.readline()))