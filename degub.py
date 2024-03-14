from itertools import chain, product
Sanjay=(3, 7)
Srinidhi=(4, 8)
Baki=list(chain(product(Sanjay, Srinidhi), product(Srinidhi, Sanjay)))
print( 'The resultant tuple : ', Baki)