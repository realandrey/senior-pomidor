def get_unique_vowels(s):
    vowels = {"a", "e", "i", "o", "u"}
    return set(s.lower()) & vowels

print(get_unique_vowels("Hello World"))  # {'e', 'o'}
print(get_unique_vowels("Python Programming"))  # {'o', 'i', 'a'}
print(get_unique_vowels("BCDFG"))
