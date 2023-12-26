# Use remove() or discard() method
sports_set = {"hockey", "cricket", "badminton", "football", "basketball"}
sports_set.remove("cricket")
print(sports_set)
print()
# If the item to remove does not exist, remove() method will raise an error
# sports_set.remove("volleyball")

# If the item to remove does not exist, discard() method will not raise an error
sports_set.discard("volleyball")
print(sports_set)
print()

# We can also use pop() method to remove an item, but this method will remove
# one item. As sets are unordered, we will not know what item got removed
x = sports_set.pop()
print(x)
print()

# clear() method empties the set
sports_set.clear()
print(sports_set)

# del keyword deletes the set completely
sports_set2 = {"hockey", "cricket", "badminton", "football", "basketball"}
del sports_set2
# print(sports_set2) # This will throw error as set has been deleted
