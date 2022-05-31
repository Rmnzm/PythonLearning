vowels = set('aeuio')
word = input("Provide a word to search for vowels: ")
found = set(word).intersection(vowels)

for vowel in found:
    print(vowel)