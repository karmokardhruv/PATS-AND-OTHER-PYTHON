rivers = {'nile': 'egypt', 'mississippi': 'united states', 'ganga': 'india', 'murray': 'austrailia', 'yangtze': 'china'}
for river, country in rivers.items():
    print("The " + river.title() + " Runs through " + country.title() + ".")
print("\nThe rivers are :")
for river in rivers.keys():
    print(river.title())
print("\nThe countries are :")
for country in rivers.values():
    print(country.title())

while True:
    age = input("How old are you? ")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15")
        break