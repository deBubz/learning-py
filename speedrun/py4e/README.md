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