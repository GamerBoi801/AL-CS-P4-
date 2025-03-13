"""#question #1


def ReadData():
    arr = []
    # Read the data from the file
    with open('Data.txt', 'r') as file:
        for line in file:
            arr.append(line.strip())
    
    return arr

def FormatArray(arr):
    concat = ''
    for word in arr:
        concat += word + ' ' #returns the cocnatenated with a space
    
    return concat

def CompareStrings(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    i = 0
    while i < min(len(str1), len(str2)):
        if ord(str1[i]) > ord(str2[i]):
            return 2
        elif ord(str1[i]) < ord(str2[i]):
            return 1
        i += 1
        
def Bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if CompareStrings(arr[j], arr[j+1]) == 2:
                #swap arr[j] & arr[j+1]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

if __name__ == '__main__':
    list_words = ReadData()
    sorted_arr = Bubble(list_words)
    print(FormatArray(sorted_arr))"""

"""#q2
class Horse():
    #constcutor
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self._Name = Name
        self._MaxFenceHeight = MaxFenceHeight
        self._PercentageSuccess = PercentageSuccess
    
    def GetName(self):
        return self._Name
    
    def GetFenceHeight(self):
        return self._MaxFenceHeight
    
    def Success(self, height, risk):
        risk_modifiers = [[5, 0.6], [4, 0.7], [3, 0.8], 2, 0.9], [1, 1]
        if height > self._MaxFenceHeight:
            return 20
        elif height <= self._MaxFenceHeight:
            for modifier in risk_modifiers:
                if risk == modifier[0]:
                    return int(self._PercentageSuccess * modifier[1])
        
class Fence(Horse): 
    def __init__(self, height, risk):
        self._height = height
        self._risk = risk

    def GetHeight(self):
        return self._height
    
    def GetRisk(self):
        return self._risk
    

        
def main():
   # list 4 2 horses
    Horses = [Horse('Beaty', 150, 72), Horse('Jet', 160, 65)] 

    Courses = []
    for i in range(4):
        height = int(input(f'Enter the height of fence {i+1}: '))
        risk = int(input(f'Enter the risk of fence {i+1}: '))
        Courses.append(Fence(height, risk))

    # Part 2(e)(i)
    for horse in Horses:
        for i, fence in enumerate(Courses):
            chance = horse.Success(fence.GetHeight(), fence.GetRisk())
            print(f"The horse {horse.GetName()} at fence {i+1} has a {chance}% chance of success")

    # Part 2(e)(ii)
    for horse in Horses:
        total_chance = 0
        for fence in Courses:
            total_chance += horse.Success(fence.GetHeight(), fence.GetRisk())
        average_chance = total_chance / len(Courses)
        print(f"The horse {horse.GetName()} has an average {average_chance}% chance of jumping over all four fences")

    # Determine the horse with the highest average chance
    highest_avg_chance = 0
    best_horse = None
    for horse in Horses:
        total_chance = 0
        for fence in Courses:
            total_chance += horse.Success(fence.GetHeight(), fence.GetRisk())
        average_chance = total_chance / len(Courses)
        if average_chance > highest_avg_chance:
            highest_avg_chance = average_chance
            best_horse = horse.GetName()
    
    print(f"The horse with the highest average chance of success is {best_horse}")


if __name__ == '__main__':
    main()

"""
#q3 linked list
null = None
LinkedList = []
FirstEmpty = 0
FirstNode = null

for i in range(0, 19):
    LinkedList.append([null, i+1])
LinkedList[19] = [null, null]

#TODO: Complete this pset
def InsertData():
     for _ in range(5):
        if FirstEmpty != null:
            nextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty