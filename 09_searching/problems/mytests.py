# iterations

# def binarysearch(mlist, target):
#     low = 0
#     high = len(mlist) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if mlist[mid] == target:
#             return mid
#         elif mlist[mid] > target:
#             high = mid -1
#         else:
#             low = mid + 1
#     return -1


def binarysearch(mlist, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if mlist[mid] == target:
        return mid
    elif mlist[mid] > target:
        return binarysearch(mlist, target, low, mid -1)
    else:
        return binarysearch(mlist, target, mid +1, high)

mlist = [1,2,3,4,5,6,7]
result = binarysearch(mlist, 8, 0, len(mlist) - 1)

if result != -1:
    print("Found")
else:
    print("Not Found")