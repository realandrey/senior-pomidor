def check_number(number):
    if number > 0:
        if number % 2 != 0:
            print(f"Число {number} положительное и нечётное.")
        else:
            print(f"Число {number} положительное и чётное.")
    elif number == 0:
        print(f"Ноль есть ноль. Чётное число, так как делится на 2 без остатка (0 ÷ 2 = 0)")
    else:
        print(f"Число {number} отрицательное.")

check_number(323)