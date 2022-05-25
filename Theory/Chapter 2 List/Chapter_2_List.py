# We have four common DATA STRUCTURES
# Lists - list()
# Dictionaries - dict()
# Typles - typle()
# Sets - set()

# EVERYTHING IN PYTHON ARE OBJECTS


LIST = []  # empty list
LIST = ['A', 'B']  # list with two elements
LIST = ['A', 1, ['B']]  # list can include different types of data

# Common list commands

LIST.append('elem')  # add elem at the end of the list
LIST.remove('elem')  # delete elem with name in brackets
LIST.pop()  # delete and return elem with index in brackets
LIST.extend(['elem1', 'elem2'])  # add list of elems to the end of the list
LIST.insert(0, 'elem')  # add elem to place with index

print(help(LIST.insert))  # command help to understand that list command do

# Copy lists
first = [1, 2, 3, 4, 5]
second = first
second.append(6)
print(second)  # [1, 2, 3, 4, 5, 6]
print(first)  # [1, 2, 3, 4, 5, 6]
# It happens because Variables "first" and "second" are links to one list
# If you want to copy list, you need to use method -copy
third = second.copy()
third.append(7)
print(third)  # [1, 2, 3, 4, 5, 6, 7]
print(second)  # [1, 2, 3, 4, 5, 6]

# To make list from string
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(
    booklist)  # ['T', 'h', 'e', ' ', 'H', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e', 'r', "'", 's', ' ', 'G', 'u', 'i', 'd', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'G', 'a', 'l', 'a', 'x', 'y']

# Slices DON'T change lists
