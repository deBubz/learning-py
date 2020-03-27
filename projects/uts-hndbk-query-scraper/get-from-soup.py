import requests
from bs4 import BeautifulSoup 
# from card import Card
import re
import sys

search_term = ""
string_arr = sys.argv[1].split()

if (len(string_arr) > 1):
    for i in range(len(string_arr)):
        if (i) < len(string_arr) - 1:
            search_term = search_term + string_arr[i] + '+'
        else:
            search_term = search_term + string_arr[len(string_arr) - 1]
else:
    search_term = string_arr[0]
    

URL = 'https://cfsites1.uts.edu.au/publications/search.cfm?scope=site&q=' + search_term
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# print(page.content)

# # name              dt.span     class="d-none"
# # desc              dd.p        class="mb-3"
# # bonus list        findall     class="f5 text-gray"

first_result = soup.find('span', class_='rs_title').getText()
print(first_result)

# # list of cards
# elements = soup.find_all('div', class_='col-sm-6 col-lg-4 mb-3 mb-sm-5')
# for e in elements:
#     # name
#     name = e.dt.span.string
#     card = Card(name)

#     # description
#     desc = e.find('p', class_='mb-3').string
#     card.card_desc = desc

#     # bonus
#     bonus_tag = e.find_all('p', class_='f5 text-gray')
#     for t in bonus_tag:
#         extract = re.search('</span> (.*)</p>', str(t)).group(1)
#         card.card_bonuses.append(extract)

#     card_list.append(card)
#     count = count + 1

# # print
# for c in card_list:
#     print(c.to_string())
# print(count, 'avaliable packages')
