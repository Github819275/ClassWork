StackVowel = ['' for i in range(100)]  # DECLARE StackVowel[0:99] : CHAR
StackConsonant = ['' for i in range(100)]  # DECLARE StackConsonant[0:99] : CHAR
VowelTop = 0  # DECLARE VowelTop : INTEGER
ConsonantTop = 0  # DECLARE ConsonantTop : INTEGER

def Pushdata(letter):
    global VowelTop, ConsonantTop
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        if VowelTop != 100:
            StackVowel[VowelTop] = letter
            VowelTop = VowelTop + 1
        else:
            print('Vowel stack full')
    else:
        if ConsonantTop != 100:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop = ConsonantTop + 1
        else:
            print('Consonant stack full')


def ReadData():
    try:
        file = open('StackData.txt', 'r')
        char = file.readline().strip()
        while len(char) > 0:
            Pushdata(char)
            char = file.readline().strip()
        file.close()
    except:
        print('File not Found!')


def PopVowel():
    global VowelTop
    if VowelTop == 0:
        return 'No data'
    else:
        VowelTop = VowelTop - 1
        return_data = StackVowel[VowelTop]
        return return_data


def PopConsonant():
    global ConsonantTop
    if ConsonantTop == 0:
        return 'No data'
    else:
        ConsonantTop = ConsonantTop - 1
        return_data = StackConsonant[ConsonantTop]
        return return_data


# Main Program
output_str = ''
ReadData()
for i in range(5):
    choice = input('vowel or consonant: ')
    if choice == 'vowel':
        catch = PopVowel()
    else:
        catch = PopConsonant()
    output_str = output_str + catch
print(output_str)
