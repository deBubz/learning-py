# 06 Strings

from [here](https://www.py4e.com/html3/06-strings)

strings are sequences of chars

```python
a = 'cheese'
a[1]                # 'h'
len(a)              # 6 - length of the string

# string traversal
for x in range(0, len(a)):
    print(letter[x])

for x in a:
    print(x)

# string slicing
a[:2]               # 'che'
a[0:2]
a[2:]               # 'ese'
a[2:5]

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

> generally strings are **immutable**, you cannot change a specific `char` in a `string`

## Extras

the method `dir(arg)`, where `arg` is a variable. The method returns a list of methods that can be applied on the variable