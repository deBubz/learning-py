# Python for Kids

## Table of Contents

- [Python for Kids](#python-for-kids)
  - [Table of Contents](#table-of-contents)
  - [Part 1 - Learning to program](#part-1---learning-to-program)
    - [Ch1 Intro](#ch1-intro)
      - [Installation](#installation)
      - [Starting](#starting)
      - [Saving your Python Programs](#saving-your-python-programs)
    - [Ch2 Calculations and variables](#ch2-calculations-and-variables)
      - [Calculating with python](#calculating-with-python)
      - [Variables](#variables)
    - [Ch3 Strings, Lists, Tuples and Maps](#ch3-strings-lists-tuples-and-maps)
      - [String](#string)
        - [Some problems with strings](#some-problems-with-strings)
        - [Embedding values in String](#embedding-values-in-string)
        - [Multiplying string](#multiplying-string)
      - [List](#list)
        - [Adding to list](#adding-to-list)
        - [Removing from list](#removing-from-list)
        - [Arithmetics in lists](#arithmetics-in-lists)
      - [Tuples](#tuples)
      - [Map](#map)
    - [Ch4 Drawing with turtles](#ch4-drawing-with-turtles)
    - [Ch5 if/else condition](#ch5-ifelse-condition)
      - [Var with no value](#var-with-no-value)
      - [String v Numbers](#string-v-numbers)
    - [Ch6 loops](#ch6-loops)
      - [For loop](#for-loop)
      - [While loop](#while-loop)
    - [Ch7 Function and Modules](#ch7-function-and-modules)
      - [Using modules](#using-modules)
    - [Ch8 Classes and Objects](#ch8-classes-and-objects)
      - [Breaking into classes](#breaking-into-classes)
      - [Defining class functions](#defining-class-functions)
      - [Try the puzzles](#try-the-puzzles)
    - [Ch9 Built-in Functions](#ch9-built-in-functions)
    - [Ch10 Useful Modules](#ch10-useful-modules)
    - [Ch11](#ch11)
    - [Ch12](#ch12)
  - [Part 2 - Bounce??](#part-2---bounce)
  - [Part 3 - not gonna write that title](#part-3---not-gonna-write-that-title)

## Part 1 - Learning to program

### Ch1 Intro

#### Installation

- **Installation** pretty self explanatory go [here (windows)](https://www.python.org/downloads/windows/), download and install the latest python3 version (2 is fine too)
- If you're **stuck** theres a [companion website](https://nostarch.com/pythonforkids) to get all the example in the book + more.
- If all else fails [google](https://www.google.com) is your best friend
- Remember to have fun, experiment.

#### Starting

> If you're stuck/ confused, feel free to ask me and or the internet for help.

- Ill start slow in this chapter to help you get used to the working environment. Then I`ll speed it up in the other chapters.
- Once installed, go ahead and launch the program `IDLE` (should be where you installed Python or search it) and you should see this. (dont worry too much if the version number is different)

```sh
Python 3.8.1 (default, Dec 21 2019, 20:57:38) 
[GCC 9.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

- This is the `Python shell`, it's integrated dev environment, where you can type in python commands to run.
- Lets try using the `print()` command to print out a string

```python
# type this in
print("Hello world")
# once you press ENTER this will be printed under
# Hello world

# The prompt (>>>) will then reappear to let you know the shell is ready to accept more commands.
```

- Make sure you surround `Hello World` correctly with double quotes `"Hello World"`. This is to tell the `print()` command that this is a `string` to print into the shell.
- **YER DID IT** congrats on your first line of code(?). You can try to experiment with the `print()` command, try mess up the spelling of different parts, using numbers, missing `"`

#### Saving your Python Programs

> I wont go through this in detail

1. In `IDLE` Choose `File` > `New Window`, a new empty window will appear with `Utitled` in the menu bar
2. Enter another `print()` command to print something
3. choose `File` > `Save`, save as `hello.py`
4. choose `Run` > `Run Module`

### Ch2 Calculations and variables

> Alot will be skimmed

#### Calculating with python 

Basicly maths, unlike the `print()` statements, which prints out what ever text inside the braces (surrounded by double quotes ofc).

To do maths, you just simply type it out in the promt `>>>` and the result will be printed

| Symbols | Operators |
|---|---|
| `+` | Add |
| `-` | Substraction |
| `*` | Multiplication |
| `/` | Division |

For order of operations use bracket `()`, **NOTE** unlike maths only round brackets are used `()`

> **NOTE** for the coding blocks below, the lines starting with `#` are comments, which the python shell will ignore.
> Comments are just notes you/other people note down to help better explain what the program does

#### Variables

**Variables** in programming describe **objects** which stores information (numbers, text, list of num/text). Have a look at this.

```python
cheese = 100
 
# Here we have a variable name "cheese" assigned with the number 100
# guess what happened when you run this

print(cheese)
```

The **Equal** operator `=` is not the same in mathematics. In programming a single `=` stand for **asign**. Where the value in the RightHandSide(`100`) is **assigned** to the variable in the LeftHandSide(`cheese`)

Now look at this

```python
square = 20
circle = 10
square = circle
print(square)           # what does this print out
                        # ans: 10
```

encorporating with some maths
```python
one = 3
two = 1
five = 6

two + five * (one - 1)  # whats the result of this equation
                        # ans: 1 + 6 * (3 - 1) = 14
```

You can try those out on `IDLE` the python shell, or run [this](./pyforkids/p1/chapt1.py)

### Ch3 Strings, Lists, Tuples and Maps

#### String

In programming, *strings* are what we call *text*, think of it as a collection of letters, numbers and symbols. In chapt 1 we used a string `"Hello World"`

We put double(or single) quotes around the text to tell python/the computer that this is a **string**.

To do multi line strings use tripple single quotes `'''` to open and close the multiline string

```python
poem = '''Roses are red
Violets are blue
Python is weird
And so are you'''

# try print it out to see if it works
```

##### Some problems with strings

There will be problems with strings which uses quotes in it. **Solution** use the 3x single quotes `'''` or **escape character** (look this up), adding a backslash `\` in front of each single/double quotes you wanted to be reprented as a string (`\'` or `\"`)

```python
triple = '''He said, "Aren't can't shouldn't wouldn't". '''
escape = "He said, \"Aren\'t can\'t shouldn\'t wouldn\'t\"."
# both of this are correct
```

##### Embedding values in String

This is to display a message(string) using the contents of a *variable* using `%s`.
It's like a **marker** for where you want to add the value (substitution).

```python
score_1 = 1234
score_2 = 333
message = "Scored %s points"
print(message % score_1)            # Scored 1234 points
print(message % score_2)            # Score 333 points  
```

> The `%s` is a place holder for another value to be embedded into the string.
> the `print(message % score_1)` tells python to 
> 1. prints out message
> 2. replaces the instance of `%s` with the value of the variable `score_1`

This for now only uses 1 variable, what about multiple variables.
Its pretty much **the same**

```python
equation = '%s plus %s equals %s'   # String using 3 variables
num_a = 3
num_b = 2

# Im sure you can work out how this works
print(equation % (num_a, num_b, num_a + num_b))
```

##### Multiplying string

pretty self explanatory, multiply a string by `x` makes the string repeats `x` times

```python
laugh = "hue "
laughing = laugh * 10
print(laughing)

spacing = ' ' * 15
print('%s This is' % spacing)
print('%s In the Middle' % spacing)
```

#### List

**Lists** are fun, most likely, you'll encounter different types of list in programming. **Lists** (generic python list) looks like this, plus some operations

```python
# this is the same as writing it on 1 line
# this spacing is to improve readability
dota_heroes = [
    "pudge" , "axe", "tidehunter", "riki", "lion"
]

# prints whole list
print(dota_heroes)
# print specific item in list
print(dota_heroes[0])           # print first item
# print subset of list from item a - b
print(dota_heroes[1:3])         # guess what is printed
# change value of a list item
dota_heroes[3] = "phantom lancer"

# list can also print numbers, mix of nums/strings, and lists of lists
nums = [3, 1, 4, 5, 5]
# # list of lists
biglist = [nums, dota_heroes]
# try printing this list out
# try figgure out how to print a specific item in biglist
```

> Look up **array index** to see why the first item of a list is `0`

##### Adding to list

use the `append` **function**, which adds an item to end of alist

```python
# using the same list above
dota_heroes = [
    "pudge" , "axe", "tidehunter", "riki", "lion"
]

dota_heroes.append("techies")   # guess what happened here
dota_heroes.append("invoker")
# print to see what changed
```

##### Removing from list

use the `del` command to delete a specific item in list

```python
# using the same list above
dota_heroes = [
    "pudge" , "axe", "tidehunter", "riki", "lion"
]

del dota_heroes[2]              # guess what happened here
# print to see what changed
```

##### Arithmetics in lists

Same in maths you can use `+` to add two lists together

> `+` can only be used to add 2 list, not a list with a number

```python
list1 = [1, 2, 3, 4]
list2 = ["one", "Two", "Three"]
list3 = list1 + list2
# print out list3 to see what happened
```

Also list can be multiplied with numbers

```python
basic = [1,2]
print(basic * 4)
```

> You cant use `` and `` on lists, you can look up why yourself

#### Tuples

Basicly the same as list but uses `()` instead of `[]`. The **difference** is tuples **cannot be changed** when they're created

#### Map

`map` (also `dict`) is a collection of things (list, tuples), the difference is **each item** has a **key** and a **corresponding value**

```python
# each items contains a
# key : value
team_comp = {
    'top' : 'deeriUS',
    'mid' : 'lux',
    'adc' : 'kog',
    'suport': 'sona',
    'jungle': 'amumu'
}

# guess what these commands does
print(team_comp['adc'])
team_comp['jungle'] = 'rammus'
del team_comp['adc']
```

> You cannot join different `maps` like `lists`

### Ch4 Drawing with turtles

basicly `import turtle` use the library to draw

### Ch5 if/else condition

`if` this is true do this, `else` if not then do this, `elif` is if else

unlike other languages

- write `and` instead of `&&`
- write `or` instead of `||`

```python 
age = 10
if age < 15:        # pay attention to the :
    print("yer a loli")
elif age > 30:
    print("yer a pedo")
else:
    print("what are you")
```

#### Var with no value

`null` is written as `None`

#### String v Numbers

```python
num = 30
fl_str = '10.3'
stingy = '30'

# string to num
conv_num = int(stingy)

# string to float
conv_fl = float(fl_str)

# num to string
conv_str = str(num)
```

> becareful when converting a float string `10.3` into an integer. An `exception` will be thrown because `int()` expected an integer

### Ch6 loops

#### For loop

you know how to use loops

```python
# for loops
for x in range (0, 5):
    print("boyo")

for x in range (0, 5):
    print("hello %s" % x)

for x in range(0, len(list_name)):
    print(list_name[x])

# using list (foreach??)
for i in list_name:
    print(i)
```

`range()` doesn't create a list of numbers, it returns an `iterator`, a type of Py object designed to work with loop
```python
# range() function
print(list(range(10,15)))
# [10, 11, 12, 13, 14, 15]
```

You know loops can be nested in another loop. So try implementing bubble sort by yourself ([answer](../misc/bubble.py))

#### While loop

let say its a combination of **loops** and **if** statements

```python
# while this is true, keep executing
x = 10
while x < 30:
    print(x)
    x = x + 2
# guess how many times this executes
```

### Ch7 Function and Modules

```python
def funcname(arguements):
    # do stuff here
    # if it returns a value add the keyword
    # if not leave out return
    return 0
```

> You know how variables and scope works.
> This could be a bit annoying with how its handled in py

#### Using modules

Import keyword

```python
# example getting input
import sys

print(sys.stdin.readline())
```

> Maybe try the puzzles?? ch4-7

### Ch8 Classes and Objects

#### Breaking into classes

Lets try this

```python
# class declaration
class Things:
  pass

# children class
class Inanimate(Things):
  pass

class Animate(Things):
  pass

# # instantiate a class
object_name = Animate()
```

#### Defining class functions

Just do it inside the scope of the class

ok you should be able to read and understand [the class example](pyforkids/p1/c8_classes.py)

#### Try the puzzles

### Ch9 Built-in Functions

```python
# Absolute
abs(10)       # 10
abs(-10)      # 10

# Bool
bool(19)      # true
bool(0)       # false
bool(-100)    # false

# dir - returns information about anything
# display functions for a list value
dir(['a', 'short'. 'list'])

# also
help()        # return documentation

# eval - run the expressions 
# often used to run user input without pasrsing
eval()

# exec - like eval but to run multilines
exec()

# open - open files
test = open('dir')
testing = test.read()
print(testing)

# writing 
test = open('dir', 'w')
test.write('input')
test.close()
```

### Ch10 Useful Modules

### Ch11

### Ch12

---

## Part 2 - Bounce??

## Part 3 - not gonna write that title

