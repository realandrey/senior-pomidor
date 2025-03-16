def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    print(result)
    return result

remove_duplicates("programming")