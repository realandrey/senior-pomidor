def longest_word(s):
    s = s.split(" ")
    longestword = max(s,key=len)
    print(longestword)

longest_word("In the middle of a vast desert, an extraordinary adventure awaits")