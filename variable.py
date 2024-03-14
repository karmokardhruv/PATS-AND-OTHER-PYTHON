x= 'global'
def foo( ) :
     global x
     y= 'Local'
     x=x*2
     print (x)
     print(y)

foo( )
