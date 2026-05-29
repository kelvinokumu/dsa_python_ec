def  tail(n):
    if n == 0:    # base case
        return 0
    print(n)
    return tail(n - 1) # recursive case

tail(5)

