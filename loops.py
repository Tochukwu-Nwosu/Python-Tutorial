"""
Question 1.
Create a program that asks the user for the following
1. A minimum number
2. A maximum number

if the maximum number supplied is less than the minimum number supplied 
    print("error)
else:
    generate a list of all prime numbers between a range of the min and max number
"""
prime_numbers = []
min_number = int(input("Enter a minimum number: "))
max_number = int(input("Enter a maximum number: "))

if (max_number < min_number):
    print("error")
else:
    for var in range(min_number, max_number + 1):
        if (var != 1):
            for divisor in range(2, var):
                if (var % divisor == 0):
                    break
            else:
                prime_numbers.append(var)
    print(prime_numbers)
        
# print(list(range(3,1)))
"""
Question 2.
Create a program that asks a user for response in brackets.
The program analyses that response and checks  if the order of brackets is correct.
if correct print("valid)
else print("Invalid)
"""