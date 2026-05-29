import random

def binary_search(values, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    print(f"mid {values[mid]} low {values[low]} high {values[high]}")
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_search(values, target, low, mid - 1)
    else:
        return binary_search(values, target, mid + 1, high)

values = random.sample(range(10, 50),10)
# values = sorted(values)
print(f"List {values}")
target = int(input("Enter value to search "))
res = binary_search(values, target, 0, len(values)-1)
if res != -1:
    print("Found")
else:
    print("Not Found")
