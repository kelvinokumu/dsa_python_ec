def a():
    print(1)
    b()
    print(4)

def b():
    print(2)
    c()
    print(5)

def c():
    print(3)
    print(6)
a()