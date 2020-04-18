import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

FILE = 'country.txt'
output = open(FILE, 'w')


## tags
elements =  soup.find_all('td', style="font-weight: bold; font-size:15px")

for e in elements:
    output.write(e.string + '\n')

print("List saved to " + FILE)

