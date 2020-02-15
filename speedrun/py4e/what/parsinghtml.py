import urllib.request, urllib.parse, urllib.error
import re
import ssl

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)

for li in links:
    print(li.decode())