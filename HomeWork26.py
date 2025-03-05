numbers = [1, 2, 3] # Задача 1
numbers.append(4)
print(numbers)

city = ["Москва", "Осака", "Париж"] # Задача 2
city.remove("Москва")
print(city)

cities = ['Москва', 'Питер', 'Екатеринбург', 'Осло'] # Задача 3
print(cities[3]) # 0 1 2 3 - счет с нуля, ожидаю 4 при индексе 3

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Задача 4
print(numbers[3:7])

colors = ["red", "green", "blue"] # Задача 5
colors[0] = "yellow"
print(colors)

animals = ['cat', 'dog', 'elephant', 'rabbit'] # Задача 6
print(len(animals))


student = {          # Задача 7
    'name' : 'Ivan',
    "age" : 20
}
student["grade"] = "A"
print(student)


student = {          # Задача 8
    'name' : 'Ivan',
    "age" : 20,
    'grade': 'B'
}
student["grade"] = "A"
print(student)


student = {          # Задача 9
    'name' : 'Ivan',
    "age" : 20,
    'grade': 'B'
}
del student['age']
print(student)


student = {          # Задача 10
    'name' : 'Ivan',
    "age" : 20,
    'grade': 'A'
}
print(student["name"])


student = {          # Задача 11
    'name' : 'Ivan',
    "age" : 20,
    'grade': 'A'
}
if "grade" in student:
    print("Ключ 'grade' найден в словаре.")
else:
    print("Ключ 'grade' не найден в словаре.")


student = {           # Задача 12
    'name' : 'Ivan',
    'address' : {
        'city' : 'Moscow',
        'street' : 'Lenina'
    }
}
student["address"]["city"] = "Saint P."
print(student)


student = {           # Задача 13
    'name' : 'Maria',
    'grades' : [75, 82, 93]
}
student["grades"][0] = 85
print(student)

students = [{          # Задача 14
    'name' : 'Ivan',
    "age" : 20
},
    {
    'name' : 'Petr',
    "age" : 22
    }]
students[1]['age'] = 56
print(students)


colors = ["red", "green", "blue"] # Задача 15
print('green' in colors)
print(len(colors))