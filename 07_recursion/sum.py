def recursive_sum(n):
    # Base case
    if n == 1:
        return 1

    # Recursive case
    return n + recursive_sum(n - 1)

res = recursive_sum(5)
print(res)