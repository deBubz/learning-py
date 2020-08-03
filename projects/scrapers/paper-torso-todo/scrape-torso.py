import re
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


#supporting functions---------------------
def get_step_count(tr):
    return tr[0].find("strong").string.replace(u'\xa0', '')


def printing(tr, t):
    print(tr[t].find_all("font")[2].string)
    print(tr[t].find_all("a"))
#---------------------

# url stuff
BASE_URL = 'http://torso.amorphous-constructions.com/instructions/2012Torso/torsoInstructionsList'
URL_GROUP = ['000to099', '100to199', '200to299', '300to399', '400to499', '500to599', '600to699', '700to731'] 
# # test with 1 link for speed
# URL_GROUP = ['000to099']

# json variables
json_data = {}
json_data['torso'] = []

#json model
# json_model = {
#     '_step': "",
#     '_instructions': []
# }


# -----------------------------------------------------------------------
# working with 1 page first
url = BASE_URL + URL_GROUP[0] + '.html'
rq = Request( url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(rq).read()
soup = BeautifulSoup(page, 'html.parser')

# scraping
steps = soup.find_all('table')

for st in range(2, len(steps) - 2):
    tr = steps[st].find_all("tr")
    print("step " + str(st - 3))

    json_model = {
    '_step': "",
    '_instructions': []
    }

    instruction_model = {
        "_note" : "",
        "_first_link" : "",
        "_sec_link" : ""
    }
    
    # im trash
    if len(tr) > 2:
        print("more than 1 instruction")
        json_model["_step"] = get_step_count(tr)
    else:
        print("single instruction")
        json_model["_step"] = get_step_count(tr)

        # note
        note = str(tr[0].find_all("font")[3].string)[1:]

        # links
        a_list = tr[0].find_all("a")

        # img_link
        first_link = str(a_list[0]).split()[1][6:-1]

        # optional vid link
        if(len(a_list) > 1):
            sec_link = str(a_list[1]).split()[1][6:-1]

            # adding secondary guide
            instruction_model["_sec_link"] = sec_link

        # adding into the model
        instruction_model["_note"] = note
        instruction_model["_first_link"] = first_link
        # what do now
        # print(tr)
        # json_model["_instructions"][0]["_note"] = 

        

        # add the instructions/ img url

    json_model["_instructions"].append(instruction_model)

    # append to the thing
    json_data['torso'].append(json_model)
    
    print()
    print('------------- st end ------------------')

print()
print("======= page end ==========")
print(json_data)

# save to json file
with open('./torso.json', 'w') as outfile:
    json.dump(json_data, outfile)
    

