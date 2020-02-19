# [08 Lists](https://www.py4e.com/html3/08-lists)

like strings(sequence of char), `list` are a sequence of mixed variables(including other lists) enclosed in `[]`

> List are mutable

## Traversing a list

```python
# Most common with a for loop
for i in numbers:
    print(i)
# or
for i in range(len(numbers)):
    print(i)
```

## List operations

Possible to:

```python
# add 2 lists together
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)        # [1, 2, 3, 4, 5, 6]
# multiply a list with an int
print([0] * 4)      # [0, 0, 0, 0]
```

## Slice Operators

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']

t[:4]       # prints 0-4
t[3:]       # prints 3-end
t[1:3]      # prints 1-3

# can also use slice to change values
t[1:4] = ['x', 'y']
# ['a', 'x', 'y', 'f']
```

## List methods

```python
# adds to end of list
t.append('d')
# extends takes a list as an arg and appends all of its elements
t1.extends(t2)
# arrange from low to high
t.sort()
# python uses tim sort
```

## Deleting elements

multiple ways of doing this

```python
# removes element at index and return removed element
li.pop(2)               # returns li[2] before removed

# simply remove the value
del li[2]
# remove more than one
del li[2:3]

# knows the elemtn but not the index
li.remove("cheese")
```

## List and functions

List also contains some built in functions to let you quickly look through list without writing loops

```python 
# return length
len(lis)

# returns highest
max(lis)

# returns lowest
min(lis)

# returns total
sum(nums)
```

## Lists and strings

Strings are **sequence of characters**, and lists are sequence of **value**. BUT list of chars are not the same as string.

```python
# split string into list of char
s = "spam"
t = list(s)

# split sentence into list of word
lis = sentence.split()

# use an arg for split() to split to string by specific seperator
lis = sentence.split(',')

# join list of strings
full_sent = " "
full_sent.join(lists)
# this case join all strings in lists seperated by a space
```

## Objects and values

This section talk `very lightly` about assignments, reference, pointers?

```python
a = 'banana'
b = 'banana'

# even though both are of the same string
# a and b referes to different objects
# to check if a and b refer 2 different objects use is operator
a is b

# same - True
# different - False
```

## Aliasing

> Refer to previous section

to use another variable to refer to a specific object, just use assignment

```python
a = [1 ,2, 3]
b = a
b is a          # true

# then b can be used to mutate a
b[0] = 3
print(a)        # [3, 2, 3]
```

## List Args

> Just stuff on good/bad way to use function args

> Also do the exercises and read the debugging section

