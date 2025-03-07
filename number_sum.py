def math(initial, max_number):
    initial = int(input("Введите число: "))
    total = 0
    while initial < max_number:
        max_number += 1
    print(initial)
    total += initial  # Добавляем число к сумме
    initial += 1

    print("Сумма чисел:", total)

math(5,int("n"))