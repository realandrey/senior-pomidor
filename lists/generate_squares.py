def generate_squares(n):
    numbers = []
    for i in range(1, n + 1):
        if i not in numbers:
            numbers.append(i ** 2)
    return numbers

print(generate_squares(5))
