#   Adding(Appending) Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print(motorcycles[0])

#   add the new element 'ducati' to the end of the list

motorcycles.append("ducati")
print(motorcycles)

cars = []
cars.append("Alto")
cars.append("cultus")
cars.append("mehran")

print(cars)

#   Inserting Elements into a List

cars.insert(0,"Liana")
print(cars)

#   Removing Elements from a List

del cars[0]
print(cars)

#   Removing Elements from a List (delete last element)

cars.pop()
print(cars)

#   Popping(removing) Items from any Position in a List

print(cars.pop(0))

#   Removing an Item by Value

cars.remove('cultus')
print(cars)

cars.append("lamborghini")
cars.append("balleno")
print(cars)

too_expensive = "lamborghini"
cars.remove(too_expensive)
print(cars)
print("\nA " + too_expensive.title() + "is too expensive hence I removed it from list")

