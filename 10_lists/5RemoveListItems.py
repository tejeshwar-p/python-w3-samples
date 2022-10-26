# Remove specified item
domestic_list = ["dog", "cat", "horse", "cow", "buffalo", "zebra", "monkey"]
domestic_list.remove("zebra")
print(domestic_list)
print()

# Remove specified index
domestic_list.pop(5)
print(domestic_list)
print()
# If no index is provided then last item is removed
domestic_list.pop()
print(domestic_list)
print()

# Remove using del keyword
wild_animals = ["crocodile", "lion", "tiger", "cheetah", "monkey"]
del wild_animals[0]
print(wild_animals)
print()

# Delete the entire list
del wild_animals
# print(wild_animals) # this will throw error because the list has been deleted
print()

# Clear the list
# This empties the list but the list still remains and has no content
apes_list = ["monkey", "orangutan", "chimpanzee", "gorilla"]
apes_list.clear()
print(apes_list)
print()

