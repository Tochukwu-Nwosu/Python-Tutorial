# Iterator
# An iterator has the __iter__() and next() method.

name = "Leonard"
# for x in name:
#     print(x)

# it = iter(name)    // converts name into an iterator
# print(type(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class MyIterator:
#     def __init__ (self, data):
#         self.data = data
#         self.index = -1
#     def __iter__ (self):
#         return self
#     def __next__ (self):
#         if self.index == len(self.data):
#             raise StopIteration
#         self.index += 1
#         return self.data[self.index]

# it = MyIterator("Aubameyang")
# print(it.__next__())