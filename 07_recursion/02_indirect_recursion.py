def a(n):
    print(f"a {n}")
    if n > 0:
        return b(n - 1)

def b(n):
    print(f"b {n}")
    if n > 0:
        return a(n - 1)

a(5)