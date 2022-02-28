
"""
1. let your program get an input from the console.
2. The input to be retrived should be asked with the prompt as 
Enter your age
3. From the age entered, calculate and print out the year of birth.
"""

# age = input("Enter your age: ")
# age_int = int(age)               #DataType conversion (From string to int)
# print(2022 - age_int)

"""
1. Create a list
2. Add the following items to the list (10, 50, 60, 70, 2)
3. Change the last item to be 29
4. Convert the list to a set 
5. Create a set with the following items (30, 10, 20, 50)
6. Find the difference between the first set and the newly created set
7. Convert the difference back to a list
8. Print the final list
"""

#list_one = [10, 50, 60, 70, 2]
# list_one[-1] = 29
# set_one = set(list_one)
# set_two = {30, 10, 20, 50}
# my_diference = set_one.difference(set_two)
# list_two = list()
# print(list_two)


names = [10, 30, 70, 20]
data = [
    {
        "entry_data" : "23-01-2020",
        "results" : [30, 100, 50, 70]
    },
    {
        "entry_data" : "24-01-2020",
        "results" : [50, 10, 20, 60]
    },
    {
        "entry_data" : "25-01-2020",
        "results" : [30, 100, 50, 90]
    }
]

data[0]['results'].append(60)    
print(data)


"""
1. Delete the entire first data
2. Remove all results from the last data and add 40 to the list
3. Update 'entry data' of the last data to 26-01-2020
4. Print data
"""

data = [
    {
        "entry_data" : "23-01-2020",
        "results" : [30, 100, 50, 70]
    }, 
    {
        "entry_data" : "24-01-2020",
        "results" : [50, 10, 20, 60]
    }, 
    {
        "entry_data" : "25-01-2020",
        "results" : [30, 100, 50, 90]
    }
]

# del data[0]

# data[-1]["results"].clear()
# data[-1]["results"] = 40

# data[-1]["entry_data"] = "26-01-2020"
# print(data)