import re
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# # # # #
# how it works
#
# for each group of steps (0-100, 101- 199)
# append tasks into the json file

# url stuff
BASE_URL = 'http://torso.amorphous-constructions.com/instructions/2012Torso/torsoInstructionsList'
URL_GROUP = ['000to099', '100to199', '200to299', '300to399', '400to499', '500to599', '600to699', '700to731'] 
# # test with 1 link for speed
# URL_GROUP = ['000to099']

# json stuff
json_data = {}
json_data['torso'] = []

total_count = 1

#---------------------
def get_step_count(tr, t):
    return tr[t].find("strong").string.replace(u'\xa0', u' ')


def printing(tr, t):
    print(tr[t].find_all("font")[2].string)
    print(tr[t].find_all("a"))
#---------------------

# scraping
# for each instruction sets
for i in range(0, len(URL_GROUP)):
    # get page
    url = BASE_URL + URL_GROUP[i] + '.html'
    rq = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(rq).read()
    soup = BeautifulSoup(page, 'html.parser')

    # scraping
    steps = soup.find_all('table')

    # print("\t>> " + str(len(steps)))

    count = 0
    addind_json = {}

    # get contents in each steps
    for st in range(2, len(steps) - 2):
        tr = steps[st].find_all("tr")

        for t in range(0, len(tr) - 1):
            # for each step
            if t == 0:  # single instruction
                # step number
                # print(tr[t].find("strong").string)

                addind_json = {
                    '_step' : get_step_count(tr, t),
                    '_instructions': [
                        {
                            '_note': tr[t].find_all("font")[2].string,
                            '_img_url': tr[t].find_all("a")[0]
                        }
                    ]
                }

                print(addind_json)

                # instruction string
                # print(tr[t].find_all("font")[2].string)

                #image.vid link
                # print(len(tr[t].find_all("a")))
                # print(tr[t].find_all("a"))
            else:       # multi instruction

                # print(tr[t].find_all("font")[2].string)
                # print(tr[t].find_all("a"))
                # print(str(tr[t]) + "\n")
                print()
                # print(addind_json['_instructions'])

                # line = tr[t].find_all("font", size=2)
                # for l in range(1, len(line)):
                #     print(line[l])
            # print()
        
        #adding 1 step
        json_data['torso'].append(addind_json)
        

        # testing
        # print(str(count) + " - " + str(len(tr)))
        count = count + 1
        # total_count = total_count + 1

        #testing first 2 step
        print("----------------------------------")
        if count == 2:
            break
    
    # break

    print()
    print("===========================")
    print(json_data)
#adding to file


    # get contents in each steps
# for each instruction sets
        


    # append to json
#     json_data['torso'].append({
#         'url' : url
#     })



# # append json
# with open('./torso.json', 'w') as outfile:
#     json.dump(json_data, outfile)
