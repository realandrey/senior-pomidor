monday = int(input("Введите количество тест-кейсов, выполненных за понедельник: "))
tuesday = int(input("Введите количество тест-кейсов, выполненных за вторник: "))
wednesday = int(input("Введите количество тест-кейсов, выполненных за среду: "))
thursday = int(input("Введите количество тест-кейсов, выполненных за четверг: "))
friday = int(input("Введите количество тест-кейсов, выполненных за пятницу: "))

summ = monday + tuesday + wednesday + thursday + friday #сумма кейсов за все рабочие дни
avg = int(summ / 5) #Формула среднего арифметичсекого округляем до целых чтобы смотрелось поприятнее

print(f"Общее количество тестов за неделю:{summ}")
print(f"Среднее количество тестов в день:{avg}")

if avg > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")