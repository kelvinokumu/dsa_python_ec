def  head(n):
    if n == 0:    # base case
        return 0
    head(n - 1)
    print(n)

head(5)
