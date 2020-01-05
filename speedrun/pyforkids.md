# Python for Kids

## Table of Contents

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

You can try those out on your shell

### Ch3 Strings, Lists, Tuples and Maps



### Ch4

### Ch5

### Ch6

### Ch7

### Ch8

### Ch9

### Ch10

### Ch11

### Ch12

---

## Part 2 - Bounce??

## Part 3 - not gonna write that title

