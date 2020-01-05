print("Chp3 strings")
print("==========")
print()

# Multiline
print("multiline wit a poem")
poem = '''Roses are red
Violets are blue
Python is weird
And so are you'''
print(poem)
print("==========")
print()

# Embedded
# # Single var
print("Single embedded var")
score_1 = 1234
score_2 = 333
message = "Scored %s points"
print(message % score_1)
print(message % score_2) 
print()
# # Multiple vars
print("Single embedded var")
equation = '%s plus %s equals %s'   # String using 3 variables
num_a = 3
num_b = 2

print(equation % (num_a, num_b, num_a + num_b))
print("==========")
print()

# Multiplying string
print("Multiplying string")
laugh = "hue "                      # notice the space after the word
laughing = laugh * 10
print(laughing)                     # try removing the space in the variable and see what changed

print()
spacing = ' ' * 15
print('%s This is' % spacing)       # See Ch3 - embedded
print('%s In the Middle' % spacing)