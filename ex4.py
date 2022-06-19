# assigns value 100 to car
cars = 100

# assigns value 4.0 to space_in_a_car
space_in_a_car = 4.0

# assigns value 30 to drivers
drivers = 30

# assigns value 90 to passengers
passengers = 90

# computes number of cars not driven and assigns it to a variable
cars_not_driven = cars - drivers

# stores number of cars with drivers(driven cars) in a variable
cars_driven = drivers

# stores the total capacity of the carpool in a variable
carpool_capacity = cars * space_in_a_car

# stores the value of average number of passengers per car driven in a variable
average_passengers_per_car = passengers / cars_driven

print("There are ", cars, " cars available")
print("There are only ", drivers, " drivers available")
print("There will be ", cars_not_driven, " empty cars today")
print("We can transport ", carpool_capacity, " people today")
print("We have ", passengers, " people to carpool")
print("We need to put about ", average_passengers_per_car, " in each car")