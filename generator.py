# Generator
# A generator posses the yield statement which contains the iter() and next() 
# Any function with the yield statement is a generator 


# def iteration_simplified (data):
#     for x in range(len(data)):
#         yield data[x]                         

# gen = iteration_simplified("Dembele")
# print(next(gen))
# print(next(gen))

# Generator Expression
# Generator Expression make use of ()
# num = [2, 4, 6, 8, 10]
# print(sum((x*x for x in num)))   # The generator expression is passed into sum method

# Exercise
name = "Tochukwu"
# reverse name string and convert to a list using both list method and generator expression

result = list((name[x] for x in range(-1, -len(name)-1, -1)))
print(result)
# Or
result2 = list((name[x] for x in range(len(name) - 1, -1, -1)))
print(result2)