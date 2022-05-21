# Original code that printing letters in word
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
for letter in word:
    if letter in vowels:
        print(letter)


# Second version
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"  # You can change this string to input result like input()
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)