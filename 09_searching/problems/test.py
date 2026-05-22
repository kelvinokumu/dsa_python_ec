import random

def BinarySearchIteration(mlist, target):
    low = 0
    high = len(mlist)-1
    while low <= high:
        mid = (low + high)//2
        if mlist[mid] == target:
            return mid
        elif mlist[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

mlist = random.sample(range(1,30),10)
mlist = sorted(mlist)
print(f"The values are {mlist} ")
target = int(input("Enter number to Search : "))
result = BinarySearchIteration(mlist, target)
if result != -1:
    print("Value found")
else:
    print("Value not found")
