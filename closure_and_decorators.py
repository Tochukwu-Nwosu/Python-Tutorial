# Closure

# def outer():
#     msg = """
#             Hello Dear,
#             This is an example of a closure.
#             """
#     def inner():
#         print(msg)

#     return inner()

# a = outer()
# print(a)

# Decorator

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        else:
            raise ValueError

        return func(a, b)

    return inner

@smart_div
def div(a, b):
    print(a / b)

div(2, 4)

'''
Task
Using decorator, create a function that will accept an argument and return the square of the passed argument.
'''

def square (func):
    def inner(a):
        a = a ** 2

        return func(a)

    return inner

@square
def find_square(a):
    return f"The square is: {a}"

print(find_square(5))