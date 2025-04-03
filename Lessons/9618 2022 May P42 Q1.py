StackData = [0 for i in range(10)]
StackPointer = 0


def output_elements():
    for i in range(StackPointer):
        print(StackData[i])
    print('StackPointer:', StackPointer)


def Push(data):
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = data
        StackPointer = StackPointer + 1
        return True


def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        return StackData[StackPointer]


# Main Program
for i in range(11):
    input_data = int(input('Enter value to add to stack: '))
    status = Push(input_data)
    if status == True:
        print('Data added to stack')
    else:
        print('Stack full. Unable to add data')

output_elements()

Pop()
Pop()
output_elements()
