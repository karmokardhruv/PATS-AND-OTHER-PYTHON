s = input("Enter a string: ")
print(len(s))
print(s*10)
print(s[0])
print(s[:3])
print(s[len(s)-3:])
print(s[::-1])
if len(s) >= 7:
   print(s[6])
else:
   print("The string is not long enough")
print(s[1:len(s)-1])
print(s.upper())
print(s.replace("a", "e"))