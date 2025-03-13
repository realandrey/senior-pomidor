def power_of(a, b=2):
    number = a
    exponent = b
    oper = number ** exponent

    if b == 2:
        print(f"Квадрат числа {a} равен {oper}.")
    else:
        print(f"Число {number} в степени {exponent} равно {oper}.")

power_of(3, 3)