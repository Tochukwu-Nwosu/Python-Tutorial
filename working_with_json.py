# Json are represented in the form of dictionaries.
import json

Interns = {
    "Zach": "zach123",
    "Victor": "victor123",
    "Tochukwu": "tochi123",
    "Jane": "jane911",
    "Bukola": "bukola270"
}

# with open("names.json", "w") as reader:
#     json.dump(Interns, reader)                         # It passes interns into the json file

print(type(Interns))
all_names = json.dumps(Interns)                        # Converts interns to a json string object and store in all_names
print(all_names)
print(type(all_names))
