def is_unique(s):
    seen = []
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    return True

print(is_unique("qwerty"))