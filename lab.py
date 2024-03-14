lab_Reading={ }
for i in range ( 0 , 5 ) :
    test_Name=input ( 'Enter test Name' )
    min=float(input ( ' Enter min value' ) )
    max=float(input ( ' Enter max value' ) )
    lab_Reading[test_Name]=(min ,max)
print(tuple(lab_Reading.items( )))
chk_Test=input('Enter check test')
obs_Value=float(input( 'Enter observed value' ))
range_Test=lab_Reading[chk_Test]
min=range_Test[ 0 ]
max=range_Test[ 1 ]
if min<obs_Value<max :
   print (' Normal ')
else:
   print (' Abnormal ')
