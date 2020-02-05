import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl

# ignore ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get all a tag
# tags = soup('a')
# for t in tags:
    # print(t.get('href', None))

tags = soup('a')
for t in tags:
    # look at parts of the tag
    print('TAG\t\t', t)
    print('URL\t\t', t.get('href', None))
    print('Contents\t', t.contents[0])
    print('Attr\t\t', t.attrs)
# ...