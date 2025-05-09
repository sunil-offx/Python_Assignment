def sum_even(n):
    return sum(i for i in range(2, n+1, 2))

print(sum_even(10))
