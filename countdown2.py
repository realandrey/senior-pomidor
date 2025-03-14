def countdown():
    count = 11
    for i in range(11):
        while count > 1:
            count -= 1
            print(count)

    print("Старт!")

countdown()