# Append items
# To add items at the end of list
animals_list = ["dog", "cat", "zebra", "horse", "elephant"]
animals_list.append("mouse")
print(animals_list)
print()

# Insert items
# To insert at specific index
domestic_list = ["dog", "cat", "horse", "cow"]
domestic_list.insert(1, "rabbit")
print(domestic_list)
print()

# Extend list
# To append elements from another list to the current list
wild_animals = ["lion", "tiger", "cheetah", "monkey"]
domestic_list.extend(wild_animals)
print(domestic_list)
print()

# Add Any Iterable
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

