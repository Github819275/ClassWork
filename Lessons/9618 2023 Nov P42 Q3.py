import datetime
class Character:
    def __init__(self, CharacterName, DateOfBirth: datetime, Intelligence, Speed):
        self.__CharacterName = CharacterName  # PRIVATE CharacterName : STRING
        self.__DateOfBirth = DateOfBirth  # PRIVATE DateOfBirth : DATE
        self.__Intelligence = Intelligence  # PRIVATE Intelligence : REAL
        self.__Speed = Speed  # PRIVATE Speed : INTEGER

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, value):
        self.__Intelligence = value

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        year = self.__DateOfBirth.year
        return 2023 - year


class MagicCharacter(Character):
    def __init__(self, CharacterName, DateOfBirth: datetime, Intelligence, Speed, Element):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.__Element = Element  # PRIVATE Element : STRING

    def Learn(self):
        if self.__Element == 'fire' or self.__Element == 'water':
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == 'earth':
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)


# Main Program
FirstCharacter = Character('Royal', datetime.datetime(2019,1,1), 70, 30)
FirstCharacter.Learn()
print('Name is', FirstCharacter.GetName())
print('Age is', FirstCharacter.ReturnAge())
print('Intelligence is', FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter('Light', datetime.datetime(2018,3,3), 75, 22, 'fire')
FirstMagic.Learn()
print('Name is', FirstMagic.GetName())
print('Age is', FirstMagic.ReturnAge())
print('Intelligence is', FirstMagic.GetIntelligence())
