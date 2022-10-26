# list objects have sort() method to sort the list alphanumerically ascending by default
fruit_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_list.sort()
print(fruit_list)
print()

# sort the list numerically
number_list = [200, 50, 65, 82, 23]
number_list.sort()
print(number_list)
print()

# sort descending using reverse = True
fruit_list2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_list2.sort(reverse=True)
print(fruit_list2)
number_list.sort(reverse=True)
print(number_list)
print()

# Custom sort function
# We can also use our own sort function using the param 'key = my_custom_function'


def my_sort_function(n):
    return abs(n - 50)


number_list2 = [100, 25, 30, 99, 89, 32, 17, 50]
number_list2.sort(key=my_sort_function)
print(number_list2)
print()

# Case-insensitive sort
fruit_list3 = ["banana", "Orange", "Kiwi", "cherry"]
fruit_list3.sort(key=str.lower)
print(fruit_list3)
print()

# Revers order
fruit_list3.reverse()
print(fruit_list3)
print()
