class Card:
    def __init__(self, number, colour):
        self.__number = number  # PRIVATE number : INTEGER
        self.__colour = colour  # PRIVATE colour : STRING

    def GetNumber(self):
        return self.__number

    def GetColour(self):
        return self.__colour


def ChooseCard():
    card_found = False
    while card_found == False:
        user_index = int(input('Enter index of card to choose: '))
        while user_index < 1 or user_index > 30:
            print('Value should be between 1 - 30 inclusive. Re-enter: ')
            user_index = int(input('Enter index of card to choose: '))
        user_index = user_index - 1
        if selected_cards[user_index] == 0:
            print('Valid')
            card_found = True
            selected_cards[user_index] = 1
        else:
            print('Already taken, Re-enter: ')
    return user_index


# Main Program
selected_cards = [0 for i in range(30)]  # 0 means cards has not been selected
card_values = []
try:
    file = open('CardValues.txt', 'r')
    number_data = file.readline().strip()
    while len(str(number_data)) > 0:
        colour_data = file.readline().strip()
        temp_card_object = Card(int(number_data), colour_data)
        card_values.append(temp_card_object)
        number_data = file.readline().strip()

    file.close()
except:
    print('No such file found')

Player1 = []
for i in range(4):
    index = ChooseCard()
    player_card = Card(card_values[index].GetNumber(), card_values[index].GetColour())
    Player1.append(player_card)
for i in range(4):
    print(Player1[i].GetNumber(), Player1[i].GetColour())
