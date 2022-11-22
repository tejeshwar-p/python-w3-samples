# A tuple is a collection which is ordered, unchangeable, indexed
# and allows duplicate values
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print()

# allow duplicates
my_tuple2 = ("apple", "banana", "apple", "cherry", "cherry")
print(my_tuple2)
print()

# tuple length
print(len(my_tuple2))
print()

# create tuple with one item
# a comma after needs to be added to create tuple with one item
this_tuple = ("apple",)
print(type(this_tuple))
print()
# NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))
print()

# tuples can be of any data types
tuple1 = ("mango", "orange", "watermelon")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
print()

# a tuple can contain different data types
tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)
print()

# tuples are defined as objects with the data type 'tuple'
print(type(tuple4))
print()

# we can also use tuple() constructor to make a tuple
this_tuple2 = tuple(("kiwi", "avocado", "grapes"))
print(this_tuple2)
print()
