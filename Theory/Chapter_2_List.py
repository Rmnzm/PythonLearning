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
