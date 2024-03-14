import re
s=input()
if re.match('c.+h$', s):
    print('Found a match')
else:
    print('Not matched')