def count_vowels(string):
    vowels = "aeiouAEIOU"  # Гласные буквы
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print(f"Количество гласных в строке '{string}': {count}")
    return count

count_vowels("Hello World!")