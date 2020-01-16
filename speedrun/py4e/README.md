# Python for Everyone

Notes following the course (here)[https://www.py4e.com]
But this README will only contains some in fo 

## 02 variables

### Some operators

```python
a = 12
b = 10

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)         # exponents
print(a//b)         # floor?
```

[chapter 2 exercises](code/02variable.py)

## 03 conditional statements

### `try` and `except` for exeptions

```python
try:
    # code
except:
    # if try breaks
```

## 04 function

### `math` module

```python
import math

math.sin(4)
math.log10(1)
```

## 05 Iteration

```python
# infinite input different way
while True:
    line = input("> ")
    if line == 'x':
        break
    print(line)

print("ending")
```

## 06 Strings

strings are sequences of chars

```python
a = 'cheese'
a[1]                # 'h'

# string traversal
for x in range(0, len(a)):
    print(letter[x])

for x in a:
    print(x)

# string slicing
a[:2]               # 'che'
a[2:]               # 'ese'

# `in` operator
'a' in 'banana'     # True
'ee' in 'banana'    # False

# str.find
a.find('s')         # 4 index of s
# also have a 2nd int arg to specify where the search start

# strip whitespace
b = '   ol   '
b.strip()           # ol
```

## 07 Files

### Persistence

This chapter cover content on how to work with Secondary Memory(files)

### Opening files

```python
try:
    fhand = open('filedir.ext') 
    print(fhand)
except:
    print("error")
```

> if `open` is successful, the os returns a **file handle**.
> Which is not the actual data but it can be used to read data.
> the **handle** is only returned if the file exist and given the proper permissions to read the file

### Text files and lines

stuff about newlines

### Reading files

while the **handle** doesnt contain file data, its easy to setup a `for` loop to read and count each of the lines in a file

```python
hand = open('mbox-short.txt')
count = 0
for line in hand:
    count = count +1
print('Line count:', count)
```




### Searching through a file

### Letting the user choose the file name

### Using `try`, `exept`, and `open`

### Writing files