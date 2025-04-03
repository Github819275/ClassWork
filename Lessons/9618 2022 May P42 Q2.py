import random


def output_elements():
    for rows in range(10):
        for cols in range(10):
            print(ArrayData[rows][cols], end=' ')
        print()


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)

    return -1


ArrayData = [[random.randint(1, 100) for i in range(10)] for j in range(10)]
output_elements()
print()
ArrayLength = 10
for X in range(ArrayLength):
    for Y in range(ArrayLength - 1):
        for Z in range(ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

output_elements()

user = int(input('Enter: '))
print(BinarySearch(ArrayData, 0, 9, user))
print(BinarySearch(ArrayData, 0, 9, 200))
