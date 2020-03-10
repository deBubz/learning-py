import random as rand

# randomly uppercase, lower each character in a string

input = list(input("Enter String: ").lower())
output = "" 

for i in range(len(input)):
    if(rand.randint(0, 1)):
        output += input[i].upper()
    else:
        output += input[i].lower()

print(output)
    
