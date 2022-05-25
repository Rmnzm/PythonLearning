vowels = ['a', 'e', 'u', 'i', 'o']
word = input()

found = {}

for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 0  # init key in dict
        found[letter] += 1

for key, value in found.items():
    print(key, 'was found', value, 'time(s).')

# input string = hello my name is Roman. I live in Russia. If you hate Russia you hate me. If you hate me, I hate you!

# printing result

# a was found 8 time(s).
# e was found 9 time(s).
# u was found 6 time(s).
# i was found 5 time(s).
# o was found 6 time(s).