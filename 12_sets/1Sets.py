# A set is a collection which is
# unordered, unchangeable, unindexed and do not allow duplicates
# Set items are unchangeable but we can add new items and remove existing items
this_set = {"Hewlett-Packard", "Dell", "MSI", "Acer"}
print(this_set)
print()

# Here duplicate values will be ignored.
this_set2 = {"one", "two", "three", "four", "four"}
print(this_set2)
print()

# length of a set
print(len(this_set))
print(len(this_set2))
print()

# Set items can be of any data type
set1 = {"pepsi", "coke", "mirinda", "thumsup"}
set2 = {1, 5, 4, 6, 20, 99}
set3 = {True, False, False}

# Set can contain different data types
set4 = {"clock", 45, True, 90, "watch"}
print(set4)
print()

# Sets are defined as object with the data type 'set'
print(type(set1))
print(type(set4))
print()

# We can also use set() constructor to make a set
set5 = set(("summer", "winter", "monsoon", "spring", "autumn"))
print(set5)
print()

# Recap -
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""