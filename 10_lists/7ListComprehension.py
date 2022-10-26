# List comprehension offers shorter syntax when you wnat to crate a new list
# based on the values of existing list
# below code is WITHOUT list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)
print()
# below code is WITH list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list2 = [x for x in fruits if "a" in x]
print(new_list2)
print()

# Syntax - new_list = ['expression' for 'item' in 'iterable' if 'condition' == True]

# condition - is like a filter that only accepts the items that evaluate to True
# iterable - can be any iterable object like list, tuple, set etc
# expression - is the current item in the iteration but it is also the outcome
#               which we can manipulate before it ends up like a list item in
#               the new list.
#             - expression can also contain conditions (like if, else)

# accept items that are not "apple"
new_list3 = [x for x in fruits if x != "apple"]
print(new_list3)
print()

# with no 'if' statement
new_list4 = [x for x in fruits]
print(fruits)
print()

# we can use range() function to create an iterable
new_list5 = [x for x in range(10)]
print(new_list5)
print()

# accept only numbers lower than 5
new_list6 = [x for x in range(10) if x < 5]
print(new_list6)
print()

# set the values in the new list to uppercase
new_list7 = [x.upper() for x in fruits]
print(new_list7)
print()

# set all values in the new list to 'hello'
new_list8 = ["hello" for x in fruits]
print(new_list8)
print()

# return orange instead of banana
new_list9 = [x if x != "banana" else "orange" for x in fruits]
print(new_list9)
print()

