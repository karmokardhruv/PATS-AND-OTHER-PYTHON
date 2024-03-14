odd_sq=[ ]
for x in range(1,11):
     if x%2==1:
       odd_sq.append(x**2)
print(odd_sq)

squares = [x**2 for x in range(1,11,2)]
print(squares)