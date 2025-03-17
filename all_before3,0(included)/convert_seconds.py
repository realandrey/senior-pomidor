def convert_seconds(a):

    minutes = (a // 60) % 60
    hours = a // 3600
    if (a % 60) > 0:
        minutes += 1

    print(f"В {a} секундах содержится {hours} час(ов) и {minutes} минут(ы).")
    return hours, minutes

a = int(input("Введите количество секунд: "))

convert_seconds(a)