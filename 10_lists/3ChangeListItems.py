# Change item value
vegetables_list = ["Onion", "Potato", "Tomato", "Green chillies"]
vegetables_list[2] = "Cucumber"
print(vegetables_list)
print()

# Change range of item values
vegetables_list[1:3] = ["Raw banana", "Ridge gourd"]
print(vegetables_list)
print()
# If we insert more items than we replace, then new items will be inserted
# where we specified, and the remaining items will move accordingly
# and the length of the list will change
vegetables_list[1:2] = ["Bottle gourd", "Ash gourd"]
print(vegetables_list)
print()
# If we insert less items than we replace, then new items will be inserted
# where we specified, and the remaining items will move accordingly
vegetables_list[1:3] = ["Carrot"]
print(vegetables_list)
print()

# To insert new item without replacing any of the existing values we can
# use insert() method
# The length of the list will change
animals_list = ["dog", "cat", "zebra", "horse", "elephant"]
animals_list.insert(1, "rabbit")
print(animals_list)
print()

