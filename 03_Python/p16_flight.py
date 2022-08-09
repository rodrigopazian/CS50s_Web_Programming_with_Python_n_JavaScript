class Flight():
    #Function that creates a Flight
    def __init__(self, input):
        self.capacity = input
        #create an empty list of passengers for the object itself
        self.passengers = []

    #Function that adds a passenger to self.passengers list
    def addPassenger(self, name):
        #add passenger to self.passengers
        self.passengers.append(name)

#Create flight number 1 flight1 with capacity of 4 passengers 
flight1 = Flight(4)

print(flight1.capacity)
print(flight1.passengers)

peoplelist = ["person1", "person2", "person3", "person4"]
for person in peoplelist:
    flight1.addPassenger(person)

print(flight1.capacity)
print(flight1.passengers)

#Create flight number 2 flight2 with capacity of 3 passengers 
flight2 = Flight(3)

print(flight2.capacity)
print(flight2.passengers)

peoplelist2 = ["person1", "person2", "person3"]
for person in peoplelist2:
    flight2.addPassenger(person)

print(flight2.capacity)
print(flight2.passengers)