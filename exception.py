'''
TYPES OF ERRORS
1. Syntax error
2. Exception :- logical
'''
'''
EXCEPTION HANDLING
try and except handles errors
'''
# print(x)      # This will give a NameError by default

try:
    print(x)
except:
    print("Undefined variable")


'''
EXERCISE
Create a class called password manager. The class should have a list called old password that holds all of the user's past password. The last item of the list is the user's current password. There should be a method called get password that returns the current password and a method called set password that sets the user's password. The set password method should only change the password if the attempted password is diffrent from all the user's past password, finally, create a method that recieves a string and returns a boolean value either true or false depending on whether the string is equal to the current password or not.
'''