from collections import Counter
s = 'Hello all 5.'
s = s.replace( ' ','')
s = s.replace( '.','')
a = s.upper( )
d = Counter(a)
marklist = sorted(d.items(), key=lambda x:x[1])
g = dict(marklist)
res = dict(reversed(list(g.items())))

for i in res:
 if i. isalpha( ) :
   print(i, res[i])