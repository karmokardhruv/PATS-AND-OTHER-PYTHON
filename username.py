dict1={'Abhiraj':'1111','Priya':'2222','Jeet':'3333'}
user=input("")
if user in dict1:
    passWORD = input("")
    if dict1[user] == passWORD:
        print('You are now logged into the system')
    else:
        print('Invalid password')
else:
    print('Not a valid user of the system')