def number_sum():
    n = int(input("Введите число: "))

    total = 0
    numbers = ""

    for i in range(1, n + 1):
        numbers += str(i) + " "  # Добавляем число в строку
        total += i  # Прибавляем число к сумме

    print("Числа:", numbers.strip())  # strip() убирает лишний пробел в конце
    print("Сумма чисел:", total)

number_sum()