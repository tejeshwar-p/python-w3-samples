# Adding values to a tuple is called "packing" a tuple
fruits = ("apple", "banana", "cherry")

# Extracting the values back into variables is called "unpacking" tuples
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print()

# If number of variables is less than the number of values
# we can add an * to the variable name and the values will
# be assigned to the variable as a list
months = ("January", "February", "March", "April", "May", "June", "July")
(one, two, *others) = months
print(one)
print(two)
print(others)
print()

# If the asterisk is added to another variable name than the last, Python
# will assign values to the variable until the number of values left matches
# the number of variables left.
(first, *others, last) = months
print(first)
print(others)
print(last)
print()

