# We can use the union() method that returns an new set containing all items
# from both sets, or the update() method that inserts all the items from one
# set into another
set1 = {"ab", "cd", "ef", "gh"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print()

set1.update(set2)
print(set1)
print()

# Both union() and update() will exclude any duplicate items

# The intersection_update() method will keep only the items that are present
# in both sets
setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}
setx.intersection_update(sety)
print(setx)
print()

# The intersection() method will return a new set, that only contains the items
# that are present in both sets
setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}
setz = setx.intersection(sety)
print(setz)
print()

# Keep all, but not the duplicates
# symmertric_difference_update() method will keep only the elements that are
# not present in both sets
setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}
setx.symmetric_difference_update(sety)
print(setx)
print()

# symmetric_difference() method will return a new set, that contains only the
# elements that are not present in both sets
setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}
setz = setx.symmetric_difference(sety)
print(setz)
print()
