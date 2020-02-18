
# [07 Files](https://www.py4e.com/html3/07-files)

## Persistence

This chapter cover content on how to work with Secondary Memory(files)

### Opening files

```python
# use try exept in case there is an error finding/openning thefile
try:
    fhand = open('filedir.ext') 
    # frints the handle not the file
    print(fhand)
except:
    print("error")
```

> if `open` is successful, the os returns a **file handle**.
> Which is not the actual data but it can be used to read data.
> the **handle** is only returned if the file exist and given the proper permissions to read the file

### Text files and lines

> stuff about newlines. [read this](https://www.py4e.com/html3/07-files#text-files-and-lines) for more info

### Reading files

while the **handle** doesnt contain file data, its easy to setup a `for` loop to read and count each of the lines in a file

```python
# open
hand = open('mbox-short.txt')
count = 0

# count line
for line in hand:
    count = count +1
print('Line count:', count)
```

If you know the file size is **smaller** thand thesize of your main memory. You could always use the `read()` methof from the file handler

```python
handler = open('file.txt')
print(handler.read())
```

> its better to store output of `read()` to a var since every call will exhaust the resource

> also `open()` should also be used if the file data fits confortably in the computers main memory

### Searching through a file

Simple, run a foreach loop through the file then use if statements to search for patterns

```python
fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('From:'):        # search for matching prefix
        print(line)
```

Now when your programs gets more complicated, you may want to use `continue` in the loops.
Basic idea is the loop is looking for specific lines and skipping others.
When the line is **found** do something with it.

```python
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    # if line starts with from is not true # hmmm
    if not line.startswith('From:'):    
        continue
    # Process our 'interesting' line
    # skips the print(line) and go to the next itteration
    print(line)
```

### Letting the user choose the file name

simply just let the user input the filename

### Using `try`, `exept`, and `open`

### Writing files

to write to files, use `'w'` as a seccond params, but if the file **did not exist**, a new one will be created.

To write, use the `write()` function of the **file handler**, make sure to **manualy** manage `newlines` when writing to file

```python
fout = open('output.txt', 'w')
fout.write("stuff\n")
fout.close()
```

and when youre done writing or using the file handler, **always** remember to `close()` it

```python
fhandler.close()
```

>> do the ex