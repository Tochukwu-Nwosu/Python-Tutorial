#Collection Data Types

#List
# countries = ["Nigeria", "Egypt", "South-Africa", "Ghana", "Togo"]
# capitals = ['Abuja', 'Cairo', 'Pretoria', 'Accra', 'Lome']

# #append operation
# countries.append("Algeria")
# capitals.append('Algiers')
# print(countries, capitals)

# #insert operation
# countries.insert(2, "Angola")
# capitals.insert(2, 'Luanda')
# print(countries, capitals)

# #pop operation
# print(countries.pop(2), capitals.pop(2))
# print(countries, capitals)

# #remove operation
# countries.remove("Algeria")
# capitals.remove('Algiers')
# print(countries, capitals)

# print(capitals.index("Cairo"))
# print(len(countries), len(capitals))
# countries.append("Egypt")
# print(countries.count("Egypt"))           # Return number of occurrences of value.

# List Comprehension
# animal_class = ['Dog', 'Cat', 'Bird']
# animal_class_with_s = [name +"s" for name in animal_class]           # [expression/variable, loop, codition:optional]
# print(animal_class_with_s)

# word = "crammed"
# letter_list = [letter for letter in word]            # what does this line do?
# print(letter_list)
# letter_list = [letter for letter in word if letter not in "aeiou"]            # what does this line do?
# print(letter_list)

# Tuples
# datatypes = ('integers', 'floating points', 'strings', 'boolean', 'list', 'tuples', 'sets', 'dictionary')


# Sets
# animals = {'Horse', 'Dog', 'Lion', 'Tiger', 'Cat', 'Elephant'}
# pets = {'Dog', 'Cat', 'Bird'}

# union Operation
# print(animals.union(pets))

# add operation
# animals.add('Bear')
# print(animals)

# difference operation
# print(animals.difference(pets))
# print(pets.difference(animals))

# intersection operation
# print(animals.intersection(pets))

# update operation
# animals.update(pets)
# print(animals)

# print(animals.issuperset(pets))
# print(pets.issubset(animals))
# print(animals.isdisjoint(pets))

# Dictionaries
# states = {
#     'Abia': 'Umuahia', 
#     'Adamawa': 'Yola', 
#     'Akwa-Ibom': 'Uyo', 
#     'Nasarawa': 'Lafia', 
#     'Kaduna': 'Kaduna', 
#     'Lagos': 'Ikeja'}

# print(states.items())
# print(states.keys())
# print(states.values())
# print(states.get('Abuja', 'Invalid key'))
# states.setdefault('Niger', 'Minna')
# states['Lagos'] = 'Lekki'
# print(states)

# Slicing
# numbers = "12345"
# region = slice(0,2)
# changed_numbers = numbers[region]
# print(changed_numbers)
# sliced_numbers = numbers[2:5]
# print(sliced_numbers)