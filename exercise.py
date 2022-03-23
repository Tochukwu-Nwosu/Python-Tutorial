"""
Create a registration and login system where we will be able to register a user or add a user to our simple database using a list which will be in a json file
and allow the user to login if the user is in our simple database.
"""
import json

username_list = []
password_list = []

with open("exercise.json", "w") as reader:
    json.dump(username_list, reader)
with open("names.json", "a") as reader:
    json.dump(password_list, reader)

class system:
    def __init__(self):
        pass
    
    def registration(self):
        print("REGISTRATION!")
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")

        # To check if username and password exist in the database else appends username and password to the database.

        if (self.username in username_list):                                     
            print("Username alredy exist!")
        elif (self.password in password_list):
            print("Password alredy exist!")
        else:
            username_list.append(self.username)
            password_list.append(self.password)
            print("Registration Completed!")
    
    def login(self):
        print("LOGIN!")
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")

        # To ensure that both username and password correspond and exist in the database.

        i = username_list.index(self.username)                                                               
        if (self.username in username_list[i] and self.password in password_list[i]):
            print("Welcome!")
        else:
            print("Wrong Login Details!")

# Testing the system
user1 = system()
user2 = system()
user3 = system()
user1.registration()
user2.registration()
user3.registration()
user1.login()
user1.login()
# user1.registration()
# user1.login()
# user2 = system()
# user2.login()
# user2.registration()
# user2.login()
# user1.login()
print(username_list)
print(password_list)