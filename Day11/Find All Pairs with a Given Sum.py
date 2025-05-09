def pairs_with_sum(lst, target):
    seen = set()
    result = []
    for num in lst:
        if target - num in seen:
            result.append((num, target - num))
        seen.add(num)
    return result

print(pairs_with_sum([1, 2, 3, 4, 5], 6))
