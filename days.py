d = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
mon = input("enter the month name = ")
print("Number of days in ",mon,"=",d[mon])

df = list (d.keys())
df.sort()
print(df)

print("Months which have 31 days are ")
for i in d:
    if d[i] == 31:
        print(i)

print("Months sorted according to number of days")
print("February")
for i in d:
    if d[i] == 30 :
        print(i)
for i in d:
    if d[i] == 31 :
        print(i)
