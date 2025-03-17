def check_string_length(string, length):
    if int(len(string)) >= length:
        print("Длина строки достаточная")
    else:
        print("Строка слишком короткая")

check_string_length("Python", 23)