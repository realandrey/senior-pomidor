def merge_lists(list1, list2):
    listmerged = list1 + list2
    return (list(set(listmerged)))

print(merge_lists([1, 2, 3, 4], [3, 4, 5]))  # [1, 2, 3, 4, 5]