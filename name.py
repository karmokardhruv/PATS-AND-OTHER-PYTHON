s= 'Dhruv'
result = s.find('a')
print(result)
print('COUNT',s.count(s))
print('UPPERCASE',s.upper())
print('conc with surnmae',s+' Karmokar')
sums=0
for i in s:
    sums=sums+ord(i)
print(sums)