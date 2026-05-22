import random

def Sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    for current_index in range(1, number_of_elements):
        current_value = unsorted_list[current_index]
        while unsorted_list[current_index - 1] > current_value and current_index > 0:
            pass

    return unsorted_list

def getValues():
    # unsortedList = [5, 4, 3, 2, 1]
    unsortedList = random.sample(range(20,100),5)
    print(f"Unordered list is : {unsortedList}")
    sortedlist = Sort(unsortedList)
    print(f"Sorted list {sortedlist}")

getValues()
