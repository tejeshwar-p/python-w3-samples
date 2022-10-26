# In python we CANNOT combine strings and numbers like this
# age = 36
# txt = "My name is John, I am " + age
# print(txt)


# We have to user format() method to format the other type to string
age2 = 36
txt2 = "My name is John, and I am {}"
print(txt2.format(age2))

# format() method takes unlimited no. of arguments and are placed into respective placeholders
quantity = 3
item_no = 567
price = 49.50
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

# we can use index numbers {0} to be sure the arguments are placed in the correct placeholders
my_order2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order2.format(quantity, item_no, price))
