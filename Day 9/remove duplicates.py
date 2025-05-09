def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 3, 3]))  # Output: [1, 2, 3] (order may vary)
