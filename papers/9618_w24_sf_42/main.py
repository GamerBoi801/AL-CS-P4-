class EventItem():
    def __init__(self, EventName, Type, Difficulty):
        self._EventName = EventName
        self._Type = Type
        self._Difficulty = Difficulty

    def GetName(self):
        return self._EventName
    
    def GetDifficulty(self):
        return self._Difficulty
    
    def EventType(self):
        return self._Type

def Character():
    def __init__(self, CharacterName, Jump, Swim, Run, Drive):
        self._CharacterName = CharacterName
        self._Jump = Jump
        self._Swim = Swim
        self._Run = Run
        self._Drive = Drive

    def GetName(self):
        return self._CharacterName
    
    def CalculateScore(self, Type, difficulty):
        chance = ''
        if Type == 'jump':
            chance =  self._Jump 
        elif Type == 'swim':
            chance =  self._Swim 
        elif Type == 'run':
            chance =  self._Run 
        elif Type == 'drive':
            chance =  self._Drive
        

        if chance  >= difficulty:
            return 100
        else:
            diff  = difficulty - chance
            if diff == 1:
                return 80
            elif diff == 2:
                return 60
            elif diff == 3:
                return 40
            elif diff == 4:
                return 20
            else:
                return 0


if __name__ == '__main__':

    Group = [
        EventItem('Bridge', 'jump', 3),
        EventItem('Water wade', 'swim', 4),
        EventItem('100 mile run', 'run', 5),
        EventItem('Gridlock', 'drive', 2),
        EventItem('Wall on wall', 'jump', 4)
    ]

    Character1 = Character('Tarz', 5, 3, 5, 1)
    Character2 = Character('Drive', 2, 2, 3, 4)
    