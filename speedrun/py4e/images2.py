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