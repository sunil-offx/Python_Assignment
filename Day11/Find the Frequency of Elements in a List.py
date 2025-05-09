from collections import Counter

def element_frequency(lst):
    return dict(Counter(lst))

print(element_frequency([1, 2, 2, 3, 1, 1]))  
