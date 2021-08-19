cars = 100
# number of cars
space_in_a_car = 4.0
# amount of space in a car
drivers = 30
# there are 30 drivers
passengers = 90
# there are 90 passengers
cars_not_driven = cars - drivers
# number of cars that aren't driven by anyone
cars_driven = drivers
# number of cars driven by drivers
carpool_capacity = cars_driven * space_in_a_car
# total capacity of driven cars
average_passengers_per_car = passengers / cars_driven
# number of passengers in a certain car


print("There are", cars, "cars available.") # this will print number of cars that are available
print("There are only", drivers, "drivers available.") # this will number of drivers available
print("There will be", cars_not_driven, "empty cars today.") # this will print the number of extra cars
print("We can transport", carpool_capacity, "people today.") # this will print the availible number for transportation
print("We have", passengers, "to carpool today.") # this will print the number of passengers that uses the carpool
print("We need to put about", average_passengers_per_car,
      "in each car.") # this will print the average number of passengers in a car