# A dictionary is ordered, changeable and do not allow duplicates
# Dictionaries are used to store data in key:value pairs
# Dictionary is ordered from Python 3.7 onwards. In Python 3.6 and earlier
# they were unordered

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)
print()

print(this_dict["brand"])
print()

# Dictionaries cannot have two items with same key
this_dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2022
}
print(this_dict2)
print()
# Here new key will replace the existing key's value

# Use len() function to determine how many items are there in dictionary
print(len(this_dict2))
print()

# The values in dictionary can be of any data types
this_dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(this_dict3)
print()

# Dictionaries are defined as objects with the data type 'dict'
print(type(this_dict3))
print()

# It is also possible to use the dict() constructor to make a dictionary
this_dict4 = dict(name="John", age=36, country="Norway")
print(this_dict4)
print()

# Recap
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""