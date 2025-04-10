class SaleData:
    def __init__(self, ID, quantity):
        self.ID = ID
        self.quantity = quantity


CircularQueue = [SaleData('', -1) for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0


def Enqueue(new_data):
    global Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = new_data
    NumberOfItems = NumberOfItems + 1
    if Tail == 4:
        Tail = 0
    else:
        Tail = Tail + 1
    return 1


def Dequeue():
    global Head, NumberOfItems
    if NumberOfItems == 0:
        return SaleData('', -1)
    return_value = CircularQueue[Head]
    NumberOfItems = NumberOfItems - 1
    if Head == 4:
        Head = 0
    else:
        Head = Head + 1
    return return_value


def EnterRecord():
    user_ID = input('Enter ID: ')
    user_quantity = int(input('Enter quantity: '))
    temp_record = SaleData(user_ID, user_quantity)
    status = Enqueue(temp_record)
    if status == 1:
        print('Stored')
    else:
        print('Full')


# Main Program
for i in range(6):
    EnterRecord()
removed = Dequeue()
if removed.ID != '':
    print('ID is', removed.ID, 'and quantity is', removed.quantity)
else:
    print('Queue Empty!')
EnterRecord()
for i in range(Head, Tail):
    temp = CircularQueue[i]
    print(temp.ID, temp.quantity)
