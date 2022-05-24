paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
# At first char to sixth char
for char in letters[:6]:  # First slice of list letters is first word
    print("\t", char)
print()
# At last char to -seventh char or 21-28
for char in letters[-7:]:  # Second slice of list letters is last word
    print("\t" * 2, char)
print()
# At 12 char to 20 char
for char in letters[12:20]:  # Third slice of list letters is middle word
    print("\t" * 3, char)
