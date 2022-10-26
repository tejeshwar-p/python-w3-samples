# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print()

# Append list2 into list1:
list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
for x in list5:
  list4.append(x)
print(list4)
print()

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
print()
