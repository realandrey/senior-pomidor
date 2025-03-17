def is_sorted(lst):
    sortedlist = sorted(lst)
    if lst == sortedlist:
        return True
    else:
        return False


print(is_sorted([1, 2, 3, 4, 5]))