# Avariable is only available from inside the region it is created. this is called scope.

# Local scope
# A variable created inside a function belongs to the local scope of the function and can only be used inside that function.
# Example
# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# Function  inside Function
# As explained in the example above, the variable x is not available outside the function but it is available for any function inside the function
# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()

# myfunc()

# Global scope
# A variable created in the main body of the python code is a global variable and belongs to the global scope.
# Global variable are available from within any scope, global and local.
#Example
# A variable created outside of a function is global and can be used by anyone
# x = 300
# def myfunc():
#     print(x)
# myfunc()
# print(x)

# Naming variables
# if you operate with the same variable name inside and outside of a function, python will treate them as two seperate variables.
# Example
# x = 300
# def myfunc():
#     x = 200
#     print(x)
# myfunc()
# print(x)

"""
Global keyword
if you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable belongs to the global scope.
"""
# def myfunc():
#     global x
#     x = 300

# myfunc()
# print(x)

"""
We can use the global keyword if you want to make a change to a global variable inside a function
Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword
"""
x = 300
def myfunc():
    global x
    x = 200

myfunc()
print(x)
