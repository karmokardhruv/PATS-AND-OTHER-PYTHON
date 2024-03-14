def isogram(a):
  k=True
  for i in a:
      if a.count(i)==1:
          k=True
      else:
          return False
  if a.isalpha() and k:
      return True
  else:
      return 'invalid'
def mini(a):
    mi=a[0]
    for i in a:
        if len(i) <len(mi):
            mi=i
    return mi
def maxi(a):
    ma=a[0]
    for i in a:
      if len(i)> len (ma) :
          ma=i
    return ma
s=list(input().split(','))
l=[]
for i in s:
    if isogram(i)==True:
        l.append(i)
    elif isogram(i)=='invalid':
        l=['invalid']
        break
if l==[]:
    print('none')
elif l==['invalid']:
    print('invalid')
else:
  print(len(l))
  print(mini(l))
  print(maxi(l))