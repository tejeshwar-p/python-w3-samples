# the pop() method removes the item with the specified key name
mango_dict = {
    "name": "Mango",
    "seasonal": True,
    "generic color": "Yellow"
}
print(mango_dict)
mango_dict.pop("seasonal")
print(mango_dict)
print()

# The popitem() method removed the last inserted item
# In versions before 3.7, a random item is removed instead
mango_dict = {
    "name": "Mango",
    "seasonal": True,
    "generic color": "Yellow"
}
print(mango_dict)
mango_dict.popitem()
print(mango_dict)
print()


