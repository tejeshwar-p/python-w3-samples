# Items in a set cannot be accessed by referring to an index or a key
# We have to use for loop
set1 = {"India", "Australia", "Canada", "United States"}
for country in set1:
    print(country)
print()

print("India" in set1)
print()

# Once a set is created, we cannot change its items, but we can add new items.
