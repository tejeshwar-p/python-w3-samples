# Adding an item to the dictionary is done by using a new index key and
# assigning a value to it
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict)
this_dict["color"] = "red"
print(this_dict)
print()

# The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added.
this_dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict2)
this_dict2.update({"color": "white"})
print(this_dict2)
print()

