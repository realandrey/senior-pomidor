def find_min(numbers):
    minmum = numbers[0]
    for i in numbers:
        if i < minmum:
            minmum = i
    print(f"Минимальное число в списке:", {minmum})
    return minmum

find_min([3, 10, 4, 3, 5])