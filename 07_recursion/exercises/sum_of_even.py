def even_sum(n):
    if n == 0:
        return 0

    return (2 * n) + even_sum(n - 1)

res = even_sum(10)
print(res)
