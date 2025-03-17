user = {
    "name" : "Andrei",
    'profession' : 'QA',
    "tool" : "swagger"
}

testtool = str(input("Введите ваш любимый инструмент для тестирования: "))
user['tool'] = testtool
if not testtool:
    print("Инструмент не указан. Попробуйте снова!")
else:
    print(f"Ваш любимый инструмент: {testtool}. Отличный выбор!")