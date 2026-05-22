def recurse(n):
    print(n)
    return recurse(n + 100)

recurse(0)