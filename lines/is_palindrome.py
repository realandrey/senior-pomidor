def is_palindrome(s):
    s = s.lower()
    result = ""

    for char in s:
        if char.isalnum():
            result += char

    print(result == result[::-1])
    return result == result[::-1]

is_palindrome("A man, a plan, a canal: Panama")
is_palindrome("racecar")
is_palindrome("hello")