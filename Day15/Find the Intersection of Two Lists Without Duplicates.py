def list_intersection(a, b):
    return list(set(a) & set(b))

print(list_intersection([1, 2, 2, 3], [2, 3, 4]))  
