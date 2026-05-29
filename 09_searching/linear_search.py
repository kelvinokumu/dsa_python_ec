import random

def linear_search(values, target):
    num_of_values = len(values)
    for index in range(num_of_values):
        if values[index] == target:
            return index
    return -1

values = random.sample(range(-9, 5),10)
print(f"List {values}")
target = int(input("Enter value to search "))
res = linear_search(values, target)
if res != -1:
    print("Found")
else:
    print("Not Found")