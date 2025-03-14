Names = [] * 10
HeadPointer = -1
TailPointer = 0 #stores the index of the free space in the queue

def Enqueue(data):
    #checks if the queue is empty using max index value
    if TailPointer  < 10:
        #item is inserted usign TailPointer
        Names[TailPointer] = data
        TailPointer += 1

        #also init the HeadPointer
        if HeadPointer == -1:
            HeadPointer = 0

    else:
        print('Queue is full')

def Dequeue(data):
    #checks if Headpointer is -1, if then the queue is empty    
    if HeadPointer == -1:
        print('Queue is empty')

    else:
        item = Names[HeadPointer]
        Names[HeadPointer] = None
        HeadPointer += 1
    
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0