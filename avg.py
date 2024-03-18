#find the average runs scored by 4 matches
print("enter the runs for four matches")
run1=int(input())
run2=int(input())
run3=int(input())
run4=int(input())
sum1=run1+run2+run3+run4
average=sum1/4
print("average", average)

#area of a circle
import math
print("enter the radius")
radius=float(input())
square=radius*radius
area=square*math.pi
print("area", area)

#calculate cost of setting up the lab
print("cost of one computer")
conec=float(input())
print("no of computers")
nofc=int(input())
print("cost of one table")
conet=float(input())
print("no of tables")
noft=int(input())
print("cost of one chair")
conech=float(input())
print("no of chairs")
nofch=int(input())
print("number of hours woked")
noh=float(input())
print("wage per hour")
wage=float(input())
Costofcomputer= conec*nofc
Costoffurniture = noft*conet + nofch*conech
Labourcost = noh*wage
totalcost=Costofcomputer+Costoffurniture+Labourcost
print("total cost for lab setup", totalcost)