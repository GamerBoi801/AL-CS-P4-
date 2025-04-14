"""Q1 """
global Jobs
Jobs = [[_ for _ in range(0, 1)] for _ in range(0, 99)]  

global NumberOfJobs

def init():
    global Jobs 
    global NumberOfJobs
    for i in range(0, 99):
        Jobs[i] = [-1,  -1]
    
    NumberOfJobs = 0

def AddJob(number, priority):
    global Jobs
    global NumberOfJobs
    for i in range(0, 99):
        if Jobs[i] == [-1, -1]:
            Jobs[i] = [number, priority]
            NumberOfJobs += 1
            print("Job added")
            return 
    print("Not Added")

def InsertionSort():
    global Jobs
    buffer = []
    n = len(Jobs)
    
    for i in range(1, n):
        key = Jobs[i]  # The current element to be inserted
        j = i - 1
        # Shift elements of Jobs[0..i-1] that are greater than key
        while j >= 0 and Jobs[j][1] > key[1]:
            Jobs[j + 1] = Jobs[j]  # Shift element to the right
            j -= 1
        
        Jobs[j + 1] = key  # Place key in its correct position
    print("Jobs sorted by priority")

if __name__ == '__main__':
    init()
    AddJob(12, 10)
    AddJob(13, 20)  
    AddJob(14, 30)
    AddJob(15, 40)
    AddJob(16, 50)
    AddJob(17, 60)
    InsertionSort()
    print(Jobs)