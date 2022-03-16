"""
Consider a module to be the same as a code library
A file containing a set of functions you want to include in your application
"""
import firstmodule
firstmodule.welcome("Tochukwu")

"""
To create a module just save the code you want in a file with the file extension .py
The module can contain functions and variables.
"""
"""
Variables in Module
The module can contain functions, as already described, but also variables of all types

Example
save this code in the file firstmodule.py
"""
person1 = {
    "name": "Zach",
    "age": 60,
    "country": "Nigeria"
}
"""
import the module named firstmopdule in mymodule, and access the person1 dictionary
import firstmopdule
value = firstmopdule.person1["name"]
print(value)
"""

"""
Naming a Module
a module must end with the .py extension

Re-naming a module
you can create an alias when you import a module, by using the keyword as:
Example
create an alias for firstmodule called fm:

import firstmodule as fm
value = fm.person1["age"]
print(value)
"""

"""
Using the dir() Function
The is a built_in function to list all the function names (or variable names) in a module. The dir()
Example 
list all the defined names belonging to the zach module.
x = dir(firstmodule)
print(x)
"""

"""
Exercise
Create a car class with method to accept and display car properties like color, name, increment fuel level.
save the file as a module, then import the file in another python file, create a class in that python file, inherit the properties
of the other class and add a simple drive method that print out a statement.
"""