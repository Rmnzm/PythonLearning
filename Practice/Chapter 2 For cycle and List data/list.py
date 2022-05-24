phrase = "Don't panic!"
letters = [i for i in phrase]

print(letters)  # ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']

print(letters[0:10:3])  # ['D', "'", 'p', 'i'] Start = letters[0], End = letters[9], Step = 3

print(letters[3:])  # ["'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']  Start = letters[3], End = letters[-1]

print(letters[:10])  # ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i'] Start = letters[0], End = letters[9]

print(letters[::2])  # ['D', 'n', 't', 'p', 'n', 'c'] Every second letter

# To make list from string
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(
    booklist)  # ['T', 'h', 'e', ' ', 'H', 'i', 't', 'c', 'h', 'h', 'i', 'k', 'e', 'r', "'", 's', ' ', 'G', 'u', 'i', 'd', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'G', 'a', 'l', 'a', 'x', 'y']

print(booklist[0:3])  # ['T', 'h', 'e']

print("".join(booklist[0:3]))  # The

print("".join(booklist[-6:]))  # Galaxy

print("".join(booklist[4:14]))  # Hitchhiker

print("".join(booklist[13:3:-1]))  # rekihhctiH
