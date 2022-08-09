class Flight():
    #Function that creates a Flight
    def __init__(self, input):
        self.capacity = input
        #create an empty list of passengers for the object itself
        self.passengers = []

    #Function that adds a passenger to self.passengers list often called a method
    def addPassenger(self, name):
        #add passenger to self.passengers only if the flight still has capacity
        #if capacity is equal 0 do not add a passenger and return False
        if self.calc_capacity() == 0:
            return False
        #if it's not 0 add a passenger and return True
        self.passengers.append(name)
        return True

    #Function that return the capacity subtracted from the number of passengers on the list
    def calc_capacity(self):
        return self.capacity - len(self.passengers)

#Create flight number 1 flight1 with capacity of 3 passengers 
flight1 = Flight(3)

print(flight1.capacity)
print(flight1.passengers)

peoplelist = ["person1", "person2", "person3", "person4"]
for person in peoplelist:
    #Add a person to the flight and get the return if it was added or not with the True or False return value
    added = flight1.addPassenger(person)
    #If it was added print that it was added successufuly
    #if added is true:
    if added:
        print(f"Added {person} to the flight successufuly")
    #if not:
    else:
        print(f"No available seats for {person} anymore")


print(flight1.capacity)
print(peoplelist)
print(flight1.passengers)