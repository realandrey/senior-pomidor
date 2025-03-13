def check_grade(score):
    if 100 >= score >= 90:
        print(f"Оценка за {score} баллов: Отлично.")
    elif 89 >= score >= 75:
        print(f"Оценка за {score} баллов: Хорошо.")
    elif 74 >= score >= 50:
        print(f"Оценка за {score} баллов: Удовлетворительно.")
    elif 50 > score:
        print(f"Оценка за {score} баллов: Неудовлетворительно.")

check_grade(90)