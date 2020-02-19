# Python for Everyone

Notes following the course (here)[https://www.py4e.com]
But this README will only contains some in

> Contains all my notes from lesson 02-17

---

## Topics

- [02 variables](notes/02-variables/README.md)
- [03 conditional statements](notes/03-conditionals/README.md)
- [04 function](notes/04-functions/README.md)
- [05 iterations](notes/05-iterations/README.md)
- [06 string](notes/06-strings/README.md)
- [07 files](notes/07-files/README.md)
- [08 Lists]()
- [09 Dictionaries]()
- [10 Tuples]()
- [12 Regex]()
- [13 Network Programming]()    
- [14 Using Web Services]()
- [15 OOP]()
- [16 Database]()
- [17 Data Visualization]()

---


 ---

## 09 Dictionaries

`dictionary` are similar to `list`. BUT in List, each element are identified by an index number.
in Dictionaries, each element are associated wit a **key** value.

> The association of akey and a value is called `key-value` pair or an `item`

All the examples in this sections will be dictionaries of `English : Spanish` words so both keys and values will be strings

```python
# ditct() creates adictionary without items
translate = dict()

# adding an item with a keyhttps://www.twitch.tv/evo
# value is uno
translate['one'] = 'uno'
```

> The item order of a *dict* at creation does *not matter*.
> If you print out the *dict* it will not return the **expected order**. 
> The item order is **unpredictable**

The `in` operator for *dict* will tell you if its a **key** in the dict.
Using values will **return `False`**

```python
'one' in translate      # True
'uni' in translate      # False

# in uses a different algorithm for list and dicts
# List uses a linear search algo    O(n)
# Dict uses a hash table            O(logn)
```

[more on hash tables](https://en.wikipedia.org/wiki/Hash_table)

> Write program that reads the word in `word.txt` and store them as keys in a dict and it doesnt matter what the values are
>
> Then use  `in` to check the keys

### Dictionary as a set of counters

Suppose given a string and you want to count how many each letter appears, Theres are several ways to achieve this

> 1. create 26 vars, traverse the string and for each corresponding char, increment the var
> 2. create a list of elem, where each char is correspond with an index number. increment the matching element
> 3. create dict with chars as keys. When first see the word, add in the dict and increment the matching key-char 

From this its clear that using a *dict* will be fastest

This is what it looks like

```python
word = "bird up"
chardict = dict()

for chars in word:
    if c not in chardict:       # not in dict, add with counter 1
        chardict[c] = 1
    else:                       # exist, increment
        chardict[c] = chardict[c] + 1
```

#### `dict.get(key, value)`

`get()` operator takes a key and **default value**. If the key **exist** -> returns the corresponding value. Else returns the **default value**

```python
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0))         # 100
print(counts.get('tim', 0))         # 0
```

with this we can more precisely write the char count program before. `get` method automaticly handles the case where a key is not a dict.

```python
word = 'bird up'
d = dict()

for chars in word:
    d[chars] = d.get(c, 0) + 1
```

### Dictionaries and files

Anothe use is to count word occurance in text file. Lets try an extraction of *Romeo and Juliet*

```md
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
```

So we need 2 `for` loops (go throuh each line, go through each word)

```python
fhand = open('file.txt')
counts = dict()

for line in fhand:
    words = line.strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
```

### Looping and Dictionaries

Just some patterns looping through the dict

```python   
# show keys with count > 10
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10 :
        print(key, counts[key])
```

```python
# print alphabetized key
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
```

### Advanced text Parsing

so removing punctuation. we can use `lower`, `punctuation`, and `translate`

> translate is pretty weird
>
> `line.translate(str.maketrans(fromstr, tostr, deletestr))`
>
> Replace the characters in `fromstr` with the character in the same position in `tostr` and delete all characters that are in `deletestr`. The `fromstr` and `tostr` can be empty strings and the `deletestr` parameter can be omitted.

we wont specify `tostr` but use `deletestr` params to delete all punctuation.

We get the list of punctuation from python `string.punctiation`

```python
import string

fhand = open("filename")
counts = dict()

for line in fhand:
    line = line.rstrip().lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

# care this might be py2.0
```

> try the excercises

---

## 10 Tuples

`Tuples` are very much similar to lists but they are **Immutable**.
Tuples are also **comparable** and **hashable** so we can sort lists of them and use as key values

```python
# basic tuple
t = ('a', 3, c)
# single elem tuple
rt = ('a',)             # Note the comma
# empty tuple
et = tuple()
```

> Also like a List you can select elem by index, splice `tuples`

> **NOTE**: you cant modify `tuple` elemts but you can replace it

```python
t = ('a', 'b', 'c')
t = ('A',) + t[1:]
# Assign t with A + tuple from index 1-end

print(t)
# ('A', 'b', 'c')
```

### Comparing Tuple

Comparison operators `<`, `>`, `==` works with sequences (`tuples`, `string`, `list` and `dict`?). It works by comparing the corresponding index between 2 sequences

```python
a = (0, 1, 3)
b = (0, 2, 4)

print( a > b )      # False
```

The `sort` func works the same way **as above**.
This feature allows it self to work as part of the `DSU` pattern

- **Decorate** create a list of tuples with the sort key **before** the element from sequence
- **Sort** sort the tuple with `sort`
- **Undecorate** extracting the sorted element 

```python
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()

# Decorate
for word in words:
    t.append((len(word), word))
# Sort
t.sort(reverse=True)
# Undecorate
res = list()
for length, word in t:
    res.append(word)
```

### Tuple Assignment

OK wtf, `tuples` allow **Left side** assignment. Allows you to assign more than one value at a time on the left side..

```python
m = ["big", "snake"]
x,y = m

print(x)        # big
print(y)        # snake

# this work because its the python translate to this
x = m[0]
y = m[1]

# for tuples
(x, y) = m
```

WTF you can do this to swap 2 variables

```python
a, b = b, a
```

> **Both Side** are `tuples`
>
> Right is a tuple of expressions, where each are assigned to the respective var on the left side.
> All the expressions on the right side are evaluated before any assignment

> **NOTE**: number of value of bothsides must be the same

> **MORE**: can be any type of sequence

### Dictionaries and Tuples

dictionaries has a method `item()` that returns alist of tupes where each is a `key-value` pair

```python
d = {'a': 10, 'b':1}
t = list(d.items())

print(t)
#   [('b', 1), ('a', 10)]
```

Its **not ordered** since its from a dictionary. BUT, now its sortable since its a list of tuples

### Multiple assignment with dictionaries

Combining `items`, [tuple assignment](#tuple-assignment), and `for` you can do this

```python
for key, val in list(d.items()):
    print(val, key)
```

This works because `items()` returns a list of tuples, while `key-value` are assigned to the `key-value` pair from the list.

### The most common words

Lets reconsider the *Romeo and Juiliet* `word counter`, We'll rewrite it to count the most comon words

```python
import string

handl = open('romeo.txt')
counts = dict()

for line in handl:
    # remove punctuations
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.lower().split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# decorate
lst = list()
for key, val in list(counts.items()):
    lst.append(val, key)

# sort
lst.sort(reverse = True)

# undecorate
for key, val in lst:
    print(key, val)
```

### Using `tuples` as keys in `dict`

Since `tuple` are `hashable`, we could use tuples as a composite key for dictionaries

Assuming for a phone book which maps `fname`, and `lname` to phone numbers. Assume all the vars are defined, We could write the `dict assignment` statement as

```python
directory[last, first] = num

# then use this to traverse
for last, first in directory:
    print(first, last, directory[last, first]) = num
```

### Sequences hmmm

> This talks about the properties and usage of sequences such as `string`, `tuples`, `list`
>
> Focuses alot about the immutability of each type of sequences. [read more](https://www.py4e.com/html3/10-tuples#sequences-strings-lists-and-tuples---oh-my)

Chapt 10 Tuples - Done

> **NOTE** Try the exercises

## 12 Regex

Lets go `regex` or rather `regular expressions`

So `py` does have a native library to handle `regex`, heres the [docs](https://docs.python.org/3/library/re.html)

Heres how it works in the simplest form with `search()`

```python
import re

handl = open('file')

for line in handl:
    line = line.strip()
    if re.search('From:', line):
        print(line)

# why does it seem so simple
```

The `search()` method will only show lines that matches the `str` in the args. Not accualy real `regex` since `line.find()` is also exactly the same.

So to truely use regex, change the args to:

```python
# ...
if re.search('^From:', line):
    print(line)

# this is equivalent with startswith('From')
# the ^ means starts with
```

### Characters matching in regex

So this will show how regex really works, also heres [a simple regex key legend](regex_hint.md)

example the regex `F..m:` will match any string starts with `F` following by any 2 char then `m:`

```python
import  re
hand = open('file.txt')
for line in hand:
    line = line.strip()
    if re.search('^F..m:', line):
        print(line)

# same as
# match any string starts with F..m
```

This is really powerful when combined with the ability to indicate that a char can be repeated multiple times by using `*` or `+` in the regex.
These means that instead of matching a single char in the string. they match 0 or more(`*`) or one or more(`+`)

```python
# ...
    if re.search('^From:.+@', line)
# matches From 
# following by one or more any char 
# follow by @
```

> Something `wildcard`

> Also look up greedy search??

### Extracting data using regex

to extract date from a string in python use `findall()` to extract the substrings that matches a `regex`. Lets try the email string again

This is a faster way than writing multiple line splitting and splicing each line.

```python
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)

print(lst)
['csev@umich.edu', 'cwen@iupui.edu']
```

> `findall()` search the string and returns a list that matches the `regex`


> `\S+@+\S` the `\S+` matches any non-white space string, then the `@` then again any `\S+` non-whitespace char

In the list there are some emails are enclosed with `<>` so lets declare what we're only interested in alpha numeric characters

```regex
[a-zA-Z0-9]\S*@\S*[a-zA-Z]
```

To translate this:

1. Starts with a single lower and uppercase chars, 0-9 `[a-zA-Z0-9]`
2. Followed by non-blank `\S*`
3. `*` instead of `+` to indicate 0 or more non-blank since its already starts with a char at **1**
4. same thing above

Here is it in action

```python
import re
hand = open('file.txt')

for line in hand:
    line.strip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
```

### Combining searching and extracting

If we want to find numbers from string such as `X-DSPAM-Confidence: 0.8475`
We can use this regex

```python
s = '^X-.*: [0-9.]+

# starting with X-
# match any char 0 or more time till :
# match any number 0-9 and . one or more times
```

While this will return all lines that matches the string above, we could then use `split()` to get the numbers. We could use regex to also **parse** the line at the sametime

Parentheses `()` are another special char in `regex`. When use with `findall()`, parens indicate while you want the whole `regex` to match but are only interested in **extracting the numbers**

```python
x = re.findall('^X\S*: ([0-9.]+)', line)
```

> The content we extracted is still a **string** and needed to be coverted to be used if you wish


### Escape Chars

Since there are a few **special characters** used in `regex` to match the begining/ end of line, we have a way to specify that we want to match that character.

just use the escape character `\`

```python
import re
x = "we recieved $10.00 for cookies"
y = re.findall('\$[0-9.]+', x)

# $10.00
```

### Regex summary

Theres some stuff, look at [the quick regex guide](regex_hint.md)

### Unix Bonus

Oh shit you can `regex` along with `grep` in this format

```bash
grep <regex> file
```

> `grep` does not support non-blank char `\S` so you might need to use the set notation

**Try the exercises later**

---

## 13 Network Programming

This chapter uses py to retrieve web pages uing HTTP, read and parse data

###  HTTP

Python has a built in library that supports HTTP, its called `socket`, this simplifies making network connections through a python program

A `socket` is very similar to files, exept a single `socket` provides a 2-way connection between 2 programs. You can both **read from**(read data from the other end) and **write to**(sent to the app on the other end) the same socket

### Simple Browser

OK lets now try to make a connection `www.pr4e.org` and send this request `GET http://data.pr4e.org/romeo.txt HTTP/1.0`

```python
import socket

mysock = socket.socket(sicket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4ne.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
```

This will connect to the server port 80, send a `GET` request, following by a carriage return and newline twice `\r\n` to signify end of request.

Then the `loop` after recieves data (512 char chunks) from the socket and `print()` it out untill `recv()` returns an empty string.

This is the output 

```txt
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2018 18:52:55 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
```

The block of text is the `header` which the web server sends to describe the doc.
One of the **requirement** while using `HTTP` is the need to send/recieve data as bytes objects instead of strings. 

The socket code above uses `decode()` and `encode()` to convert string to bytes and vice versa

> Next section we'll use `b''` to notify a variable should be stored as **a byte object** (equivalent with `encode()`)

### Image over HTTP

Consider [this program](images.py).
When ran, this program will return image data and this header (after the image??)

```txt
...
Header length 393
HTTP/1.1 200 OK
Date: Wed, 11 Apr 2018 18:54:09 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Mon, 15 May 2017 12:27:40 GMT
ETag: "38342-54f8f2e5b6277"
Accept-Ranges: bytes
Content-Length: 230210
Vary: Accept-Encoding
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: image/jpeg
```

As the program runs, we dont get the `5120` chars each time calling `recv()`. We get as manychar as it is sent across the network by the webserver(**depends on your network speed**) the moment of calling `recv()` 

We can slowdown the rate of calling `recv()` using `time.sleep()`. This way so the server can "get ahead", sends more data before calling `recv()` again.

> There is a buffer between the server making `send()` requests and our application making `recv()` request.
> When a program runs with the delay in place, The server might fill up the **buffer** in the socket and be forced to pause untill our program starts to empty the buffer. The **pause** is called **flow control**

### Retrieving webpages with `urllib`

While we can manually send and recieve data over `HTTP` using `socket`, theres a simpler way to do this using `urllib`

`urllib` can treat your page like a file, Just indicate what you webpage you want to recieve and `urllib` candles all the HTTP protocol and header details

```python
# equivalent to using socket
import urllib.request

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in hand:
    print(line.decode().strip())
```

> **Difference** is `urllib` will not show/consume the **header**

### Reading binary files using `urllib`

**Binary files** are non-text files such as images, videos. The data of these files are generally not useful to print out as text, but you can **make a copy** ofa url to a local file using `urllib`

```python
import urllib.error, urllib.request, urllib.parse

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
hand = open('cover3.jpg', 'wb')
hand.write(img)
hand.close()import urllib.request, urllib.parse, urllib.error
 
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
hand = open('cover3.jpg')
```

> the program stores data returned from the network in the variable `img`.
> Then you opens and write that data into the **write-only** (`wb`) file named `cover3.jpg`

However, this will cause trouble if the file is relatively large (video) when your computer runs out of memory. To prevent this, its better to split and recieve that data in blocks(**buffer**) and then write each block to disk before retrieving the next block.

```python
import urllib.error, urllib.request, urllib.parse

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
hand = open('cover3.jpg', 'wb')
size = 0

while True:
    info = img.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    hand.write(info)

print(size, 'char coppied')
hand.close()
```

### Parsing HTML and scraping the web

A common use of `urllib` is to scrape the web. **Web scraping** is to retrieve data from the pages, examining the data looking for patterns

### Parsing HTML using regex

lets try to extact the link url from this using this regex `href="http[s]?://.+?"`

```html
<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>
```

The regex looks for:

1. string starts with `href="http://` or `href="https://`
2. then one or more chars `.+?`
3. `[s]?` matches 0 or more in the set, so `http` or `https`

see the [code here](parsinghtml.py)

> the `ssl` lib allows the program to access website that strictly enforce `HTTPS`.
> `read()` returns HTML source code as a byte object instead of returning an `HTTPResponse` obj.

Regular `regex` works fine when your page is well formatted and predictable. **BUT** since theres a lot of 'broken' html pages out there, a solution only using regex might miss out some data, or returns bad data.

This can be solve by using a robust HTML parsing library

### Parsing HTML using `BeautifulSoup`

OK so we'll use `ursllib` to read and use `BeautifulSoup` to extract `href` attributes from the `<a>` t

[code here](soup.py)

The program prompt for a web url, then opens the page and return the value of `href` attributes of the `anchor` t

Heres an update to the code to pull out other parts of each t:

```python
# ...
tags = soup('a')
for t in tags:
    # look at parts of the t
    print('TAG', t)
    print('URL', t.get('href', None))
    print('Contents', t.contents[0])
    print('Attr', t.attrs)
# ...
```

to know more youre, better off experimenting and reading the doccuments of the parsers.

the built in html parser python has is `html.parser`

> Ples do the exercises

---

## 14Using Web Services

---

## 15 OOP

---

## 16 Database

---

## 17 Data Visualization