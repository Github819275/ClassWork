class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


def outputNodes(sp):
    current_pointer = sp
    while current_pointer != -1:
        print(linkedList[current_pointer].data)
        current_pointer = linkedList[current_pointer].nextNode


def addNode(link, sp, el):
    if el == -1:
        return False, link, el
    else:
        item = int(input('Enter value: '))
        current_pointer = sp
        while current_pointer != -1:
            previous_pointer = current_pointer
            current_pointer = link[current_pointer].nextNode

        link[el].data = item
        new_node = el
        el = link[el].nextNode
        link[new_node].nextNode = -1
        link[previous_pointer].nextNode = new_node
        return True, link, el


# Main Program
linkedList = []
linkedList.append(node(1, 1))
linkedList.append(node(5, 4))
linkedList.append(node(6, 7))
linkedList.append(node(7, -1))
linkedList.append(node(2, 2))
linkedList.append(node(0, 6))
linkedList.append(node(0, 8))
linkedList.append(node(56, 3))
linkedList.append(node(0, 9))
linkedList.append(node(0, -1))
startPointer = 0
emptyList = 5

outputNodes(startPointer)
status, linkedList, emptyList = addNode(linkedList, startPointer, emptyList)
if status:
    print('Data added')
else:
    print('Data not added')
outputNodes(startPointer)
