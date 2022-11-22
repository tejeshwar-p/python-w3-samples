# Access Tuple items
this_tuple = ("tomato", "onion", "potato")
print(this_tuple[1])
print()

# Negative Indexing
print(this_tuple[-1])
print()

# Range of Indexes
this_tuple2 = ("cat", "dog", "horse", "rabbit", "parrot", "fish", "tortoise")
print(this_tuple2[2:5])
print(this_tuple2[:4])
print(this_tuple2[2:])
print()

# Range of Negative Indexes
print(this_tuple2[-4:-1])
print()

# Check if Item Exists
if "rabbit" in this_tuple2:
    print("Yes, 'rabbit' is in the fruits tuple")
print()
