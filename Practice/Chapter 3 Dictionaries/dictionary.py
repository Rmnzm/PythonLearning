found = {}
found['a'] = 0
found['e'] = 0
found['u'] = 0
found['i'] = 0
found['o'] = 0
print(found)

for k in sorted(found):
    print(k, 'was found', found[k], 'time(s).')
print()

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')