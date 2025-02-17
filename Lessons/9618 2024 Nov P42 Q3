HighScores = [['', '', ''] for i in range(7)]


def ReadData():
    try:
        file = open('HighScoreTable.txt', 'r')
        for i in range(7):
            for j in range(3):
                line = file.readline().strip()
                HighScores[i][j] = line
        file.close()
    except:
        print('File not found.')


def OutputHighScores(arr):
    for i in arr:
        print(i[0], 'reached level', i[1], 'with a score of', i[2])


def SortScores():
    for i in range(7):
        for j in range(6):
            if HighScores[j][1] < HighScores[j+1][1]:
                temp0, temp1, temp2 = HighScores[j][0], HighScores[j][1], HighScores[j][2]
                HighScores[j][0], HighScores[j][1], HighScores[j][2] = HighScores[j+1][0], HighScores[j+1][1], HighScores[j+1][2]
                HighScores[j + 1][0], HighScores[j + 1][1], HighScores[j + 1][2] = temp0, temp1, temp2

    for i in range(7):
        for j in range(6):
            if HighScores[j][1] == HighScores[j+1][1]:
                if HighScores[j][2] < HighScores[j + 1][2]:
                    temp0, temp1, temp2 = HighScores[j][0], HighScores[j][1], HighScores[j][2]
                    HighScores[j][0], HighScores[j][1], HighScores[j][2] = HighScores[j + 1][0], HighScores[j + 1][1], \
                    HighScores[j + 1][2]
                    HighScores[j + 1][0], HighScores[j + 1][1], HighScores[j + 1][2] = temp0, temp1, temp2

ReadData()
print('Before')
OutputHighScores(HighScores)
SortScores()
print('After')
OutputHighScores(HighScores)
