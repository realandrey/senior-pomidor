def dict_to_lists(my_dict):
    keylist = list(my_dict.keys())
    valuelist = list(my_dict.values())
    return keylist, valuelist
my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))