def PrintArray(arr):
    output_string = ''
    for i in range(25):
        output_string = output_string + str(arr[i]) + ' '
    print(output_string)


def LinearSearch(value):
    count = 0
    for i in range(25):
        if DataArray[i] == value:
            count = count + 1
    return count


DataArray = [0 for i in range(25)]  # 25 integer elements

try:
    file = open('Data2.txt', 'r')
    line = file.readline().strip()
    i = 0
    while len(line) > 0:
        DataArray[i] = int(line)
        i = i + 1
        line = file.readline().strip()
    file.close()
except FileNotFoundError:
    print('File not found!')

PrintArray(DataArray)

user_input = int(input('Enter a number between 1 and 100 inclusive: '))
while user_input < 0 or user_input > 100:
    print('Not in range')
    user_input = int(input('Enter a number between 1 and 100 inclusive: '))
number_count = LinearSearch(user_input)
print(f'The number {user_input} is found {number_count} times.')
