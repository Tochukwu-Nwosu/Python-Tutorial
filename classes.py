
# class calculator:

#     name = "Calculator Design"                                          #class variable

#     def __init__(self, first_num, second_num):                          #Initialization function(constructor method): It helps to define the objects of the class 
#         self.first_num = first_num
#         self.second_num = second_num

#     def add(self):                                                      #Instance method
#         return self.first_num + self.second_num

#     def multiply(self):
#         return self.first_num * self.second_num

#     @classmethod                                                        #class method
#     def show():
#         print("This is a class method.")

#     @staticmethod                                                       #static method
#     def view():
#         print("This is a static method.")

# casio = calculator(2, 4)                                                #Instantiation of the class: creating an object of the class

# print(casio.add())                                                      #Calling the method of the object
# print(casio.multiply())



""" 
1. Write a python class named rectangle constructed by a length and a width and a method which will compute the area of the rectangle
2. Write a python class named circle constructed by a radius and two methods which will compute the area and the perimeter of the circle.
"""

# class rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area (self):
#         return self.length * self.width


# PIE = 3.14159
# class circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         result = PIE * self.radius ** 2
#         result = float("{:.2f}".format(result))
#         return result

#     def perimeter(self):
#         result = 2 * PIE * self.radius
#         result = float("{:.2f}".format(result))
#         return result



# result1 = rectangle(2,4)
# print(result1.area())

# result2 = circle(3)
# print(result2.area())
# print(result2.perimeter())


"""
Create a registration and login system where we will be able to register a user or add a user to our simple database using a list
and allow the user to login if the user is in our simple database.
"""

# username_list = []
# password_list = []

# class system:
#     def __init__(self):
#         pass
    
#     def registration(self):
#         print("REGISTRATION!")
#         self.username = input("Enter Username: ")
#         self.password = input("Enter Password: ")

#         # To check if username and password exist in the database else appends username and password to the database.

#         if (self.username in username_list):                                     
#             print("Username alredy exist!")
#         elif (self.password in password_list):
#             print("Password alredy exist!")
#         else:
#             username_list.append(self.username)
#             password_list.append(self.password)
#             print("Registration Completed!")
    
#     def login(self):
#         print("LOGIN!")
#         self.username = input("Enter Username: ")
#         self.password = input("Enter Password: ")

#         # To ensure that both username and password correspond and exist in the database.

#         i = username_list.index(self.username)                                                               
#         if (self.username in username_list[i] and self.password in password_list[i]):
#             print("Welcome!")
#         else:
#             print("Wrong Login Details!")


# user1 = system()
# user2 = system()
# user3 = system()
# user1.registration()
# user2.registration()
# user3.registration()
# user1.login()
# user1.login()
# # user1.registration()
# # user1.login()
# # user2 = system()
# # user2.login()
# # user2.registration()
# # user2.login()
# # user1.login()
# print(username_list)
# print(password_list)

# CLASS INHERITANCE

# class Parent:
#     def car(self):
#         print('I have a car')

# class Child(Parent):
#     pass

# object1 = Child()
# object1.car()

# Multiple Inheritance

# class Grand_Father:                                             
#     def house(self):
#         print('I have a house')

# class Father:
#     def car(self):
#         print('I have a car')

# class Son(Grand_Father, Father):
#     pass

# first_son = Son()
# first_son.house()
# first_son.car()

# Alternative

# class Grand_Father:                                             
#     def house(self):
#         print('I have a house')

# class Father(Grand_Father):
#     def car(self):
#         print('I have a car')

# class Son(Father):
#     def car(self):
#         print("Son's car")

# second_son = Son()
# second_son.car()                                                            # Method overriding: child class overides the parent class

# class A:
#     def __init__(self):
#         print("in A class")

# class B(A):
#     def __init__(self):
#         print("in B class")

# b1 = B()

# Using super method to call A init method                            # Super method is used to call a method of the parent class in the child class
# class A:
#     def __init__(self):
#         print("in A class")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("in B class")

# b2 = B()

# class A:
#     def __init__(self):
#         print("in A class")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("in B class")

# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("in C class")

# c1 = C()                                                # Method resolution

"""
 Polymorphism
Ways of implementing polymorphism
1.Duck Typing 2.Operator Overloading 3.Method Overloading 4.Method Overriding
"""
# Duck Typing
# class Grand_Father:                                             
#     def car(self):
#         print("GrandFather's Car")

# class Father:
#     def car(self):
#         print("Father's Car")

# class Son:
#     def house(self, parent):
#         parent.car()

# parent = Grand_Father()
# parent = Father()
# son1 = Son()
# son1.house(parent)

# Operator Overloading
# In operator overloading, operator remain same but the operand changes
# a = 7                                     # same as a = int(7)  : a is an object of class int with a value of 7
# b = 5                                     # same as a = int(5)  : b is an object of class int with a value of 5
# print(a + b)
# print(int.__add__(a, b))                  # __add__ is a method in class int

# Abstraction
# Abstraction is the ability to hide non-essential details of  a class. It provides a template for other classes.

# from abc import ABC, abstractclassmethod

# class parent(ABC):                                      # An abstract method 
#     @abstractclassmethod
#     def su(self):
#         print("Parent class")

# class son(parent):                                      # Making use of an abstract method
#     def su(self):
#         print("son class")


# Encapsulation: this describes the concept of bounding data and method within a single unit
# Access Modifiers

# class Employee:
#     def __init__(self, name, salary, age):
#         self.name = name                                 # name is made public
#         self.__salary = salary                           # salary is made a private variable: two underscore. It cannot be accessed directly
#         self._age = age                                  # age is made protected: it can be accessed by the child class
#     def show(self):
#         print(self.__salary)


# emp = Employee("Victor", 10000, 70)
# print(emp.name)
# print(emp._age)
# emp.show()     # Or
# print(emp._Employee__salary)


"""
1. Create an account class with details, deposit, withdraw, details contain (name, age, sex, account_number, balance)
2. Using a class explain the concept of inheritance, polymorphism, encapsulation, and abstraction.
"""
# class Account:
#     def __init__(self):
#         pass
#     def details (self):
#         self.name = input("Enter your name: ")
#         self.age = input("Enter your age: ")
#         self.sex = input("Enter your sex: ")
#         self.account_number = input("Enter your account number: ")
#         self.balance = float(input("Enter your account balance: "))
#     def deposit (self):
#         deposit_amount = float(input("Enter amount to deposit: "))
#         self.balance += deposit_amount
#         self.balance = float("{:.2f}".format(self.balance))
#         print("Account Balance: NGN", self.balance)
#     def withdraw (self):
#         withdraw_amount = float(input("Enter amount to withdraw: "))
#         if (withdraw_amount <= self.balance):
#             self.balance -= withdraw_amount
#             self.balance = float("{:.2f}".format(self.balance))
#             print("Account Balance: NGN", self.balance)
#         else:
#             print("Insuficcient Fund")


# customer = Account()
# customer.details()
# customer.deposit()
# customer.withdraw()


from abc import ABC, abstractclassmethod

class Account (ABC):
    def __init__ (self):
        self.name = input("Enter your name: ")
        self._account_number = input("Enter account number: ")
        self.__bvn = input("Enter your BVN: ")
        self._account_balance = float(input("Enter account balance: "))

    @abstractclassmethod
    def transaction (self):
        print("This is an abstract method")
    
class customer(Account):
    def __init__ (self):
        super(). __init__()
    def transaction (self):
        print("This is an abstract method")

customer1 = customer()    
print(customer1.name)
print(customer1._account_number)
print(customer1._Account__bvn)
print(customer1._account_balance)