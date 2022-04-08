# def func():
#     print('Hello!')
#     return 0

# func()    # Calling a function executes the operation in the function but does not print the return
# print(func())  # It prints the the operation in the function and the return

# def my_func():
#     global x        # x becomes a global variable which can be viewed outside the function.
#     x = 10
#     y:any
#     print(x)

# my_func()
# print(x)

# def greet(name, msg = " welcome to python programming language!"):              # A default value is assign to the parameter msg.
#     print("Hello " + name + msg)

# greet("Tochukwu")
# greet("Tochukwu", " welcome to python tutorial!")

# def greet(msg = " welcome to python programming language!", name):            # NOTE: Non-default arguments should precede default arguments
#     print("Hello " + name + msg)

# The use of keyword-arguments(kwargs) can change the order(position) of arguments
# def my_function(num_first, num_second, num_third):
#     print('The first number is ' + num_first)

# my_function(num_third= '67', num_second= '45', num_first= '98')                    # Arguments are sent as key and value 

"""
Create a function that returns the factorial of a number
"""
# def factorial(num):
#     result = 1
#     while num != 0 :
#         result *= num
#         num -= 1
#     return result

# print(factorial(0))

"""
Create a function that takes an arbitrary parameters of numbers 
1. Iterate through those numbers
2. Your function should only return a list of prime numbers from the previous list
Hint: 
    def check_primes(number_list):
        pass
"""
# def is_prime(number):
#     if number == 1:
#         return False
#     else:
#         for divisor in range(2, number):
#             if (number % divisor == 0):
#                 return False
#         else: 
#             return True

# def check_primes(*numbers):
#     primes = [num for num in numbers if is_prime(num)]
#     return primes


# print(check_primes(1,10,20,17,13))

# Default Arguments
# Keyword Arguments
# def highest_length_name(name_1, name_2, name_3, name_4):
#     names_list = [name_1, name_2, name_3, name_4]
#     max = ""
#     for name in names_list:
#         max = name if len(name) > len(max) else max

#     return max

"""
Assignment
1. Create a function that reverses an Integer
2. Create a function that takes an arbitrary list of numbers and returns a list of all roman numeral converts.
"""
# 1
# def reverse_Integer(number):
#     str_number = str(number)
#     reversed_number = str_number[len(str_number)::-1]                         # slicing
#     print(int(reversed_number))

# reverse_Integer(400)

# 2
# def to_roman(number):
#     numbers = (1,4,5,9,10,40,50,90,100,400,500,900,1000,5000)
#     roman_numbers = ('I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M','M','V')
#     i = len(numbers)-1
#     roman =''
#     while number != 0:
#      if number >= numbers[i]:
#          roman += roman_numbers[i]
#          number -= numbers[i]
#      else:
#          i -= 1
#     return roman

# # x= int(input('enter number: '))
# # print(to_roman(x))

# def parse_numbers_list(*numbers):
#     roman_list = [to_roman(num) for num in numbers]
#     return roman_list

# numbers = input()

# Special/magic/dunder methods
# They are in-biult methods, example __str__(), __int__() and so on.