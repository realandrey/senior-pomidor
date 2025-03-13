def count_items(*args):
    count = len(args)
    print(count)

count_items(1, 2, 3, 4, 5)
count_items("apple", "banana", "cherry")  # Количество переданных элементов: 3.
count_items()