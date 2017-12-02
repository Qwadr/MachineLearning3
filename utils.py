def union_two_dict(dict1, dict2):
    union_dict = {k: dict1.get(k, 0) + dict2.get(k, 0)
                  for k in set(dict1) | set(dict2)}
    return union_dict


def sum_of_dict_values(dictionary):
    summa = 0
    for value in dictionary.values():
        summa += int(value)
    return summa
