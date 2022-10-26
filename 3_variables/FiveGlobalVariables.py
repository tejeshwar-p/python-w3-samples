# Here x is global scope variable
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


def my_fantastic_func():
    # Here x is local scope variable
    x = "fantastic"
    print("Python is " + x)


my_fantastic_func()


# Inorder to create a global variable inside a function
# we can use global keyword
def my_global_declaring_func():
    # This will declare/override the existing global
    global x
    x = "amazing"


my_global_declaring_func()
print("Python is " + x)

