import firstmodule
value = firstmodule.person1["name"]
print(value)

import firstmodule as fm
value = fm.person1["age"]
print(value)


from firstmodule import welcome
welcome("Tochi")

import firstmodule
x = dir(firstmodule)
print(x)