def find_missing(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

print(find_missing([1, 2, 4, 5]))  
