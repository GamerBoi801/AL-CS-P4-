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

#q2
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
    
    def Success(self):
        return self._PercentageSuccess

class Fence: 
    def __init__(self, height, risk):
        self._height = height
        self._risk = risk

    def GetHeight(self):
        return self._height
    
    def GetRisk(self):
        return self._risk

        
def main():
    # list 4 2 horses
    Horses = [Horse('Beaty', 150, 72), Horse('jet', 160, 65)]
    

if __name__ == '__main__':
    main()