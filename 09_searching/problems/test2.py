import random

def binaryrecursion(mlist, target):
    
    low = 0
    high = len(mlist) - 1
    while low <= high:
        mid = (low + high) // 2
        if mlist[mid] == target:
            return mid
        elif mlist[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def get_values():
    mlist = random.sample(range(-10,20),10)
    mlist = sorted(mlist)
    print(mlist)
    target = int(input("Enter value to search : "))
    # result = binaryrecursion(mlist, target, 0, len(mlist) - 1)
    result = binaryrecursion(mlist, target)

    if result != -1:
        print(f"Found at index {result}")
    else:
        print("Not Found")
    
get_values()
