peoplelist = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

print("Not sorted: ")
print(peoplelist)

#Function that takes the key "name" and gives back the value to pass inside the method sort()
def nameValues(person):
    return person["name"]

peoplelist.sort(key=nameValues)
print("Sorted by name: ")
print(peoplelist)


#Function that takes the key "house" and gives back the value to pass inside the method sort()
def nameValues(person):
    return person["house"]

peoplelist.sort(key=nameValues)
print("Sorted by house: ")
print(peoplelist)

#Simplifying the code using the lambda Function in Python that allows for single line functions to go inside
# argument and/or method fields
# lambda substitutes the name of the function
nameValues
peoplelist.sort(key=lambda person: person["name"] )
print("Sorted by house with lambda function: ")
print(peoplelist)