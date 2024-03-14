def func1( ):
    for i in range (10) :
        print(i)

def func2( ):
    i=100
    func1( )
    print(i)
func1( )
func2( )