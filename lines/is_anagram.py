from collections import Counter

def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return (Counter(s1) == Counter(s2))

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))