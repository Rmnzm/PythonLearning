phrase = "Don't panic!"  # create string
plist = list(phrase)  # string in list
print(phrase)  # print string
print(plist)  # print list string

for i in range(4):  # delete 4 last elems "nic!"
    plist.pop()

plist.pop(0)  # delete "D" from list
plist.remove("'")  # delete apostrof from list
plist.extend([plist.pop(), plist.pop()])  # move places for two objects. First of all elems unpacks from list, second elems add to list
plist.insert(2, plist.pop(3))  # unpack space and add to index 2

new_phrase = ''.join(plist)  # list into string
print(plist)  # print list
print(new_phrase)  # print string from list
