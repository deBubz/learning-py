import requests
from bs4 import BeautifulSoup
from card import Card

URL = 'https://education.github.com/pack'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# find by id
# results = soup.find(id='unity')

# find cards
elements = soup.find_all('div', class_='col-sm-6 col-lg-4 mb-3 mb-sm-5')
for e in elements:
    tag1 = e.dt.span
    tag2 = e.dd.span
    print(tag1)
    print()
    print(tag2)  
    break

# name              dt.span     class="d-none"
# desc              dd.p        class="mb-3"
# bonus list        findall     class="f5 text-gray"