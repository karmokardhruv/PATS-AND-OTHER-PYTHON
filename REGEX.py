import re
REGNO = input('')
if re.search("[0-9]{2}[A-Z]{3}[0-9]", REGNO):
    print("valid")
else:
    print("invalid")
NAME = input('')
if re.search("[A-Z]{1}[a-z]", NAME):
    print("valid")
else:
    print("invalid")

a = ['SCOPE', 'SENSE', 'SMBS']
b=input('')
if b in a:
    print("valid")
else:
    print("invalid")

import re
phone = input('')
if re.search("^[0-9]{10}$", phone):
    print("valid")
else:
    print("invalid")