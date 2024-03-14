capitals={}
for i in range (int (input ('enter the number of capitals u want to enter: - '))):
    country=input ('enter the country: - ')
    capital=input('enter the capital')
    capitals [country ]=capital
print (capitals)

countries_capital_to_be_displayed=input('enter the capital to be displayed' )
if countries_capital_to_be_displayed in capitals:
    print (capitals [countries_capital_to_be_displayed])
else :
    print ('Not known')