def search_for_vowels(phrase: str) -> set:
    """выводит гласные, найденные во введенном слове."""
    vowels = set('aeuio')
    return vowels.intersection(set(phrase))


print(search_for_vowels("sdjgnsldnklwetwe"))  # word = sdjgnsldnklwetwe  return = e
print(search_for_vowels("sky"))  # return = set()


def search_for_letters(phrase: str, letters: str = 'aeuio') -> set:  # letters with default value
    """выводит буквы, найденные во введенной фразе."""
    letters = set(letters)
    return letters.intersection(set(phrase))


print(search_for_letters("hello world", "ol"))  # return = {'o', 'l'}
print(search_for_letters("hello world"))  # return = {'o', 'e'}
print(search_for_letters(letters="ghjb", phrase="hello world yeah"))  # named arguments
print(search_for_letters("hello world", "ol"))  # positional arguments

# page 208
