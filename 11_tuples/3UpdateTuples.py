# Tuples are unchangeable, or immutable as it also is called.
# But workaround is -  we can convert the tuple into a list, change the list,
# and convert the list back into a tuple.

sample_tuple = ("New York", "Delhi", "London", "Paris")
print("Before: ")
print(sample_tuple)
sample_list = list(sample_tuple)
sample_list[2] = "Chennai"
sample_tuple = tuple(sample_list)
print("After: ")
print(sample_tuple)
print()

# Add Items
sample_list2 = list(sample_tuple)
sample_list2.append("London")
sample_tuple = tuple(sample_list2)
print(sample_tuple)
print()

# Add tuple to a tuple
sample_tuple2 = ("Fedora", "Red Hat", "Ubuntu", "Mint")
sample_tuple3 = ("Kali",)
sample_tuple2 += sample_tuple3
print(sample_tuple2)
print()

# Remove items
list3 = list(sample_tuple2)
list3.remove("Red Hat")
sample_tuple2 = tuple(list3)
print(sample_tuple2)
print()

del sample_tuple2
print(sample_tuple2)  # This will throw error because tuple is deleted

