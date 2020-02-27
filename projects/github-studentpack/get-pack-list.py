import re
import urllib.request

# ---
class Pack:
    def __init__(self, p, d, b):
        self.package_name = p
        self.description = d
        self.bonus = b

# ---

handler = urllib.request.urlopen("https://education.github.com/pack")
count = 0
packages = list()

for l in handler:
    # if not re.search('<dt id=.*</div>',str(l)): continue
    count = count + 1
    # print(l)
    x = re.findall('<dt id=\"(.*)\"', str(l))
    # pack = Pack(x[0], 'a', 'b')
    # packages.append(pack)
    print(x)

# for i in packages: print(i.package_name, i.bonus)
print(count)
