arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]


def linearSearch(value):
    for i in range(10):
        if arrayData[i] == value:
            return True
    return False


def bubbleSort():
    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


# Main Program
input_value = int(input('Enter an integer value: '))
status = linearSearch(input_value)
if status:
    print('Value Found')
else:
    print('Value Not Found')
