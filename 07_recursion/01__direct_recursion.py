def  direct(n):
    if n == 0:    # base case
        return 0
    print(n)
    return direct(n - 1) # recursive case

direct(5)
