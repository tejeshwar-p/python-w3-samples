# List items are indexed and we can access them by referring to the index number
test_list_one = ["testItem1", "testItem2", "testItem3"]
print(test_list_one[1])
print()

# Negative indexing
# -1 refers to the last item,
# -2 refers to the last second item
print(test_list_one[-3])
print()

# Range of indexes
# When specifying a range, the return value will be a new list with the specified items.
# start index is included and end index is excluded
test_list_two = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(test_list_two[2:5])
print()
# Range of negative indexes
print(test_list_two[-4:-1])
print()

# Check if item exists
if "kiwi" in test_list_two:
    print("Yes, 'kiwi' is in the fruits list")
print()



