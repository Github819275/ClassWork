class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question  # PRIVATE question : STRING
        self.__answer = answer  # PRIVATE answer : INTEGER
        self.__points = points  # PRIVATE points : INTEGER

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, user_answer):
        if user_answer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return  0


arrayTreasure = []


def readData():
    try:
        file = open('TreasureChestData.txt', 'r')
        question = file.readline().strip()
        while len(question) > 0:
            answer = int(file.readline().strip())
            points = int(file.readline().strip())
            object_treasure = TreasureChest(question, answer, points)
            arrayTreasure.append(object_treasure)
            question = file.readline().strip()
        file.close()
    except:
        print('File Not Found.')


# Main Program
readData()
question_number = int(input('Enter Question Number(1-5): '))
print(arrayTreasure[question_number - 1].getQuestion())
user_answer = int(input('Enter Answer: '))
attempts = 1
while not arrayTreasure[question_number - 1].checkAnswer(user_answer):
    user_answer = int(input('Enter Answer: '))
    attempts = attempts + 1

points = arrayTreasure[question_number - 1].getPoints(attempts)
print(points)
