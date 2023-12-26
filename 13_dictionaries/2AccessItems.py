# Accessing of items of dictionary can be done by referring to its key name in
# square brackets
laptop_details = {
    "brand": "Dell",
    "model": "Latitude 5501",
    "year": 2020,
    "RAM": "16GB"
}
value = laptop_details["model"]
print(value)
print()

# The get() method also will give us the same result
value = laptop_details.get("model")
print(value)
print()

# The keys() method will return a list of all the keys in the dictionary
keys = laptop_details.keys()
print(keys)
print()
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected
# in the keys list.

# Adding a new item to the original dictionary updates the key list
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
keys = car_dict.keys()
print(keys)
car_dict["color"] = "white"
print(keys)
print()

# The values() method will return a list of all the values in the dictionary
values = car_dict.values()
print(values)
print()

# When we make a change in the original dictionary the values list get updated as well
print(values)  # before
car_dict["year"] = 2020
print(values)  # after
# Adding a new item to the original dictionary also updates the values list
car_dict["window tint"] = "green"
print(values)
print()

# The items() method will return each item in a dictionary as tuples in a list
items = car_dict.items()
print(items)  # before modifying existing item
# Any change made in the original dictionary is reflected in the items list and
# gets updated as well
car_dict["year"] = 2022
print(items)  # after modifying existing item
# Adding a new item also updates the items list
car_dict["speed"] = "200 Kmph"
print(items)  # after adding new item
print()

# Check if key exists
if "model" in car_dict:
    print("Yes, 'model' is one of the keys in this car_dict dictionary")
print()
