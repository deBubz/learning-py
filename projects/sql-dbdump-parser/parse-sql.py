import re

output = open('datadict.csv', 'w')
    
with open('./db_baseSchema.sql') as f:
    for line in f:
        l = line.strip()
        if re.match('^CREATE', l):          # db name
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
