import requests
from bs4 import BeautifulSoup 
import re
import sys

search_term = ""
string_arr = sys.argv[1].split()

# parse query string
# dont worry about this if just using number
if (len(string_arr) > 1):
    for i in range(len(string_arr)):
        if (i) < len(string_arr) - 1:
            search_term = search_term + string_arr[i] + '+'
        else:
            search_term = search_term + string_arr[len(string_arr) - 1]
else:
    search_term = string_arr[0]
    
# soup stuff
URL = 'https://cfsites1.uts.edu.au/publications/search.cfm?scope=site&q=' + search_term
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# done
first_result = soup.find('span', class_='rs_title').getText()
print(first_result)
