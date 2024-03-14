string= input()
print(string)
char={}
for i in string:
    if i in char:
        char[i]=char[i]+1
    else:
        char[i] = 1
result= max(char, key = char.get)
print("Most frequent character:",result)