def group_by_first_letter(strings):
    dict = {}
    for string in strings:
        first_letter = string[0] # Берём первый символ строки

        if first_letter not in dict:
            dict[first_letter] = []

        dict[first_letter].append(string)

    return dict

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
