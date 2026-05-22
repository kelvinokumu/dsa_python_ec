import random

def getMaxMin(unsorted_list):
    minimum = unsorted_list[0]
    for item in unsorted_list:
        if item < minimum:
            minimum = item

    print(f"Minimum {minimum}")


def getValues():
    unsorted_list = random.sample(range(1,100),5)
    # unsorted_list = [5, 4, 3, 2, 1]
    print(f"Unordered list is : {unsorted_list}")
    getMaxMin(unsorted_list)

getValues()
