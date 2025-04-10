Animals = ['' for i in range(10)]
Animals[0] = 'horse'
Animals[1] = 'lion'
Animals[2] = 'rabbit'
Animals[3] = 'mouse'
Animals[4] = 'bird'
Animals[5] = 'deer'
Animals[6] = 'whale'
Animals[7] = 'elephant'
Animals[8] = 'kangaroo'
Animals[9] = 'tiger'

def SortDescending():
    ArrayLength = len(Animals)
    for X in range(ArrayLength - 1):
        for Y in range(ArrayLength - X - 1):
            if Animals[Y][0] < Animals[Y + 1][0]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp


SortDescending()
for i in range(len(Animals)):
    print(Animals[i])
