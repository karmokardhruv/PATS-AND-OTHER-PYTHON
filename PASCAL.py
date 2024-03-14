c = int(input())
def Pascalt(c):
   a = [1]
   b = [0]
   for x in range(c) :
      print(a)
      a =[left +right for left, right in zip(a+b, b+a)]
   return c>=1
Pascalt(c)