"""#q1 
Animals = [""] * 10


def Mid(String, Start, Quantity):
    temp  = []
    i = Start
    for i in range(Quantity):
        temp.append(String[i])
    return ''.join(temp)

def SortDescending():
    ArrayLength = 0
    Temp = ""
    ArrayLength = len(Animals)
    for x in range(0, ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            if Mid(Animals[y], 0, 1) > Mid(Animals[y+1], 0, 1) :
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp


if __name__ == '__main__':
    Animals[0] = "horse"
    Animals[1] = "lion"
    Animals[2] = "rabbit"
    Animals[3] = "mouse"
    Animals[4] = "bird"
    Animals[5] = "deer"
    Animals[6] = "whale"
    Animals[7] = "elephant"
    Animals[8] = "kangaroo"
    Animals[9] = "tiger"


    SortDescending()
    print(Animals)
"""
"""#2
class SaleData():
    def __init__(self, id, quantity):
        self._id = id
        self._quantity = quantity


CircularQueue = [SaleData("", -1) for _ in range(5)]
Head, Tail = 0, 0
NumberOfItems = 0

def Enqueue(record: SaleData):
    global NumberOfItems, Head,Tail
    if NumberOfItems == len(CircularQueue):
        return -1
    CircularQueue[Tail] = record
    
    if Tail == len(CircularQueue) - 1:
        Tail = 0
    else:
        Tail += 1

    NumberOfItems += 1
    return 1

def Dequeue():
    global NumberOfItems, Tail, Head
    if NumberOfItems == 0:
        return SaleData("", -1)
    
    item = CircularQueue[Head] #returning the first item in the queue
    Head = (Head +1) % len(CircularQueue)
    NumberOfItems -= 1
    return item

def EnterRecord():
    id = input('Please Enter a valid ID: ')
    quantity = int(input(
        "quantity: "
    ))


    if Enqueue(SaleData(id, quantity)) == 1:
        print('stored')
    else:
        print('Full')


if __name__ == '__main__':
    for i in range(6):
        EnterRecord()

    result = Dequeue()
    if result._id == "" and result._quantity == -1:
        Dequeue()
    else:
        print(f'{result._id} && {result._quantity}')

    EnterRecord()
    
    for record in CircularQueue:
        print(f'{record._id} && {record._quantity}')"""

#q3
class Employee():
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self._HourlyPay = HourlyPay
        self._EmployeeNumber = EmployeeNumber
        self._JobTitle = JobTitle
        self._PayYear2022 = [0.0 for _ in range(0, 51)]

    def GetEmployeeNumber(self):
        return self._EmployeeNumber

    def SetPay(self, WeekNumber, numberOfHours):
        pay = float(self._HourlyPay * numberOfHours)
        self._PayYear2022[WeekNumber] = pay

    def GetTotalPay(self):
        i = 0
        total = 0.0
        while self._PayYear2022[i] != 0.0:
            total += float(self._PayYear2022[i])
        
        return total

class Manager(Employee):
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValue):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self._BonusValue = BonusValue


    def SetPay(self, WeekNumber, num_of_hrs):
        percentage_increase = float(self._BonusValue / 100 )