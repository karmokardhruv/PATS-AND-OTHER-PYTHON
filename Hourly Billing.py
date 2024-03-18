print ("enter num of hours")
hour = int(input())
print ("enter num of minutes")
min = int(input())
if (hour> 7) :
    print ("Invalid input")
elif hour>=5:
    amount = 200
    hour = hour - 5
    amount = amount+hour*50+min
    print (amount)