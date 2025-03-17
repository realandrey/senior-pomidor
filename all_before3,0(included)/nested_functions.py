def calculator(a, b):

    if c == "+":
        def summ(a, b):
            summa = a + b
            print(f'Результат: {summa}')

        summ(a, b)

    elif c == "-":
        def subtraction(a, b):
            sub = a - b
            print(f'Результат: {sub}')

        subtraction(a, b)

    elif c == "*":
        def multiplication(a, b):
            mul = a * b
            print(f'Результат: {mul}')

        multiplication(a, b)

    else:
        def division(a, b):
            div = a/b
            print(f'Результат: {div}')

        division(a, b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Выберите операцию (+, -, *, /): ")

calculator(a, b)