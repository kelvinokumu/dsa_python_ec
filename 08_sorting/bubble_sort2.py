import random

def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index -= 1
    return list

def getValues():
    # unsortedList = [5, 4, 3, 2, 1]
    unsortedList = random.sample(range(1,10),5)
    print(f"Unordered list is : {unsortedList}")
    sortedlist = bubble_sort(unsortedList)
    print(f"Sorted list {sortedlist}")

getValues()