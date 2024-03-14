invitations=["Mikey", "Lewis", "Dennis"]
for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
print("People, just found a bigger table and more people will be joining us this evening")
print()
invitations.insert(0, "Shelby")
invitations.insert(2, "Amanda")
invitations.append("Duke")
for invitation in invitations:
    print("Welcome to my dinner party {}".format(invitation))
