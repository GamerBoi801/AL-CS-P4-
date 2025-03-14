#q1
"""class EventItem():
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

    p1, p2 = 0, 0

    for event in range(5):
      char1_score = Character1.CalculateScore(Group[event].EventType(), Group[event].GetDifficulty()) 
      char2_score = Character2.CalculateScore(Group[event].EventType(), Group[event].GetDifficulty())

      if char1_score > char2_score:
          p1 += 1
          print(f'{Character1.GetName()} wins {Group[event].GetName()}')
       elif char1_score < char2_score:
           p2 += 1
           print(f'{Character2.GetName()} wins {Group[event].GetName()}')
       else:
           print(f'{Character1.GetName()} and {Character2.GetName()} draw in {Group[event].GetName()}')
"""

"""#q
null = -1
class Queue():
    def __init__(self):
        self._QueueArray = [-1] * 100
        self._HeadPointer = -1  #sotres index of first data
        self._TailPointer = 0    # stores nex free location


def Enqueue(TheQueue, data):
    if TheQueue._HeadPointer == -1:
        TheQueue._QueueArray[TheQueue._TailPointer] = data
        TheQueue._HeadPointer = 0
        TheQueue._TailPointer += 1
        return 1
    
    elif TheQueue._TailPointer > 99:
        return null
    else:
        TheQueue._QueueArray[TheQueue._TailPointer] = data
        TheQueue._TailPointer += 1
        return 1
    
def ReturnAllData(TheQueue):
    line = ''
    head_counter = 0
    while TheQueue._QueueArray[head_counter] != -1:
        line += str(TheQueue._QueueArray[head_counter]) + ' '
        head_counter += 1
    return line

if __name__ == '__main__':
    TheQueue = Queue()
    inputs = [10,9,8,7,6,5,4,3,2,1]
    for i in inputs:
        Enqueue(TheQueue, i)
    print(ReturnAllData(TheQueue))"""

#q3

def ReadData(HighScores):
    with open('HighScoreTable.txt', 'r') as file:
        for i in range(7):
            HighScores[i][0] = file.readline().strip()
            HighScores[i][1] = int(file.readline().strip())
            HighScores[i][2] = int(file.readline().strip())

def OutputData(HighScores):
    for i in range(7):
        for j in range(3):
            print(HighScores[i][j])

def SortSuccess(HighScores):
    count = 0
    length = len(HighScores)
    for i in range(length):
        for j in range(0, length - i- 1):
            if int(HighScores[j][2]) < int(HighScores[j+1][2]):
                thatplayerId =  HighScores[j][0]
                game_level = HighScores[j][1]
                score = HighScores[j][2]
                #SWAP all the values 
                HighScores[j][0] = HighScores[j+1][0]
                HighScores[j][1] = HighScores[j+1][1]
                HighScores[j][2] = HighScores[j+1][2]
                HighScores[j+1][0] = thatplayerId
                HighScores[j+1][1] = game_level
                HighScores[j+1][2] = score
                count += 1
    print(f'Number of swaps: {count}')  
    return HighScores

HighScores = [[None for _ in range(3)]for _ in range(7)]
ReadData(HighScores)
OutputData(HighScores)
SortSuccess(HighScores)
OutputData(HighScores)