# Lists are used to store multiple items in a single variable
# Lists are one of the 4 built-in data types in python used to store collections of data
# Other 3 are - Tuple, Set, Dictionary
# List items are ordered, changeable and allow duplicate values
this_list = ["apple", "banana", "cherry"]
print(this_list)
print()

# Ordered
# List has defined order and order will not change.
# New items are placed at the end of the list.
# There are some list methods that will change the order,
# but in general the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items
# in a list after it has been created

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value
this_list2 = ["apple", "banana", "cherry", "banana", "cherry"]
print(this_list2)
print()

# List length
print(len(this_list))
print()

# List Items - Data type
# List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types
list4 = ["abc", 34, True, 40, "male"]
print(list4)
print()

# Lists are defined as objects with the data type 'list'
my_list = ["strawberry", "mango", "watermelon"]
print(type(my_list))
print()

# list() constructor can also be used to create list
my_list2 = list(("Google", "Amazon", "Facebook"))
print(my_list2)
print()

# Python Collections
# List -        Ordered     | Changeable        | Allows Duplicates
# Tuple -       Ordered     | Unchangeable      | Allows Duplicates
# Set -         Unordered   | Unchangeable*     | No Duplicates
# Dictionary -  Ordered**   | Changeable        | No Duplicates

# *Set items are unchangeable but items can be added or removed.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
