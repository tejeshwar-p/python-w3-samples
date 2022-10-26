# We CANNOT copy a list by simply typing list2 = list1
# because list2 will only be a reference to list1
# in this way changes reflected in list1 will also be reflected in list2
fruit_list = ["banana", "Orange", "Kiwi", "cherry"]
other_fruit_list = fruit_list.copy()
print(other_fruit_list)
print()

# Another way to copy is using list() method
another_fruit_list = list(fruit_list)
print(another_fruit_list)
print()
