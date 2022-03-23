# Working with files
# Creating a new file
# file = open("Example.txt", "x")
# Write to a file
# file = open("Example.txt", "w")
# file.write("Tochukwu")
# file.close()                          # Closing a file
# append
# file = open("Example.txt", "a")
# file.write(" Nwosu")
# file.close()
# Reading a file
# file = open("Example.txt", "r")
# print(file.read())
# file.close()

# file = open("Example.txt", "w")
# print(file.write("Tochukwu\n"))
# print(file.write("Jane\n"))
# print(file.write("Zach\n"))
# print(file.write("John\n"))
# print(file.write("Bukola"))
# file.close()

file = open("Example.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readlines())
print(file.read(5))
file.close()

# This more safe because it automatically close the file for you
with open("Example.txt", "r") as reader:
    print(reader.read())

with open("Example.txt", "w") as reader:
    print(reader.write("Demo"))