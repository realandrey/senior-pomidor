def remove_duplicates(lst):
    return(list(set(lst)))

print(remove_duplicates([9,9,1,1,3,3,4,2,4,6,7,7,2]))


def remove_duplicates2(lst):
    clearlist = []
    for item in lst:
        if item not in clearlist:
            clearlist.append(item)
    return clearlist

print(remove_duplicates2([9,9,8,8,8,1,1,3,3,4,2,4,6,7,7,2]))