#list
listnames = ["Harry", "Ron", "Hermione", "Ginny"]
lenghtlist = len(listnames)

#tuple
coordenate = (10.0, 20.0)
lenghttuple = len(coordenate)

#set
setnumbers = set()
setnumbers.add(1)
setnumbers.add(2)
setnumbers.add(3)
lenghtset = len(setnumbers)

#dict
coordenates = {"x" : 10.0, "y" : 20.0, "z" : 30.0}
lenghtdict = len(coordenates)

print(f"The list has {lenghtlist} elements.")
print(f"The tuple has {lenghttuple} elements.")
print(f"The set has {lenghtset} elements.")
print(f"The dict has {lenghtdict} elements.")