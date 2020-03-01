import requests
from bs4 import BeautifulSoup
from card import Card
import re

URL = 'https://education.github.com/pack'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
card_list = list()
count = 0

# name              dt.span     class="d-none"
# desc              dd.p        class="mb-3"
# bonus list        findall     class="f5 text-gray"

# find cards
elements = soup.find_all('div', class_='col-sm-6 col-lg-4 mb-3 mb-sm-5')
for e in elements:
    # name
    name = e.dt.span.string
    card = Card(name)

    # description
    desc = e.find('p', class_='mb-3').string
    card.card_desc = desc

    # bonus
    bonus_tag = e.find_all('p', class_='f5 text-gray')
    for t in bonus_tag:
        extract = re.search('</span> (.*)</p>', str(t)).group(1)
        card.card_bonuses.append(extract)

    card_list.append(card)
    count = count + 1

# print
for c in card_list:
    print(c.sh_detail())
print(count, 'avaliable packages')
