vowels = ['a', 'e', 'u', 'i', 'o']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')
