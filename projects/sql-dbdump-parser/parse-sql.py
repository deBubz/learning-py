import re

tbl_count = 0
file_name = "datadict.csv"
output = open(file_name, 'w')
    

for line in open('./db_baseSchema.sql'):
    l = line.strip()
    if re.match('^CREATE', l):          # db name
        tbl_count = tbl_count + 1
        sent = l.split(' ')[2]
        db_name = sent[1:len(sent) - 1]
        output.write(db_name + '\n')
    elif re.match('^\`',l):             # db attr
        sent = l[:len(l) - 1]
        attrs = ','.join(sent.split(' '))
        output.write(attrs + '\n')
    elif re.match('^PR', l):            # pk
        pk_list = l[13:len(l) - 1]
        output.write(pk_list + '\n\n')

print("saved to " + file_name)
print("There are " + str(tbl_count) + " tables.")
