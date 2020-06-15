motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modify
motorcycles[0] = 'ducati'
print(motorcycles)

# Add
motorcycles.append('ducati')
print(motorcycles)

# append makes it easy to start with an empty list.
motor = []
motor.append('honda')
motor.append('yamaha')
motor.append('suzuki')
print('motor: ' + str(motor))


# Inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an Item using del statement
del motorcycles[0]
print(motorcycles)

#removing an Item using pop() method
poppend_motorcycle = motorcycles.pop()
print(poppend_motorcycle)
print(motorcycles)

#removing an Item from any position in the list 
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

#removing an Item by value
motorcycles.remove('yamaha')
print(motorcycles)

