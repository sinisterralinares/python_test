# This code will return an error because the sort method does not know
# which presenter field to use when sorting
# presenters = [{"name": "Susan", "age": 50}, {"name": "Christopher", "age": 47}]

# presenters.sort()
# print(presenters)

#################################

# Sort alphabetically
presenters = [{"name": "Susan", "age": 50}, {"name": "Christopher", "age": 47}]

presenters.sort(key=lambda item: item["name"])
print("-- alphabetically --")
print(presenters)

# Sort by length of name (shortest to longest)
presenters.sort(key=lambda item: len(item["name"]))
print("-- length --")
print(presenters)

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# make a function that always triples the number you send in
def myfunc1(n):
    return lambda a: a * n


mydoubler = myfunc1(3)

print(mydoubler(11))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# method to sort, remember it's much easier to use the lambda function instead
def sorter(item):
    return item["age"]


presenters = [{"name": "Susan", "age": 50}, {"name": "Christopher", "age": 47}]
presenters.sort(key=sorter)
print(presenters)
