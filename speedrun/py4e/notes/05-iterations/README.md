# 05 Iteration

from [here](https://www.py4e.com/html3/05-iterations)

```python
# infinite input different way
while True:
    line = input("> ")
    if line == 'x':
        break
    print(line)

print("ending")
```

## using `continue`

`continue` is to **end** the current iteration(care of scope) and skip to the **next** iteration. 

> often used together with a condition `if` statement to do something special

```python
while True:
    line = input('> ')
    # if the first char is #, skip and ask for another input
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

[Chapt 05 exercises](05loopy.py)
