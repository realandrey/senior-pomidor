def check_age(age):
    year = int(input("Введите год вашего рождения: "))
    age = 2025 - year
    print(f"Ваш возраст: {age}")
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif 18 < age < 66:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

check_age("age")