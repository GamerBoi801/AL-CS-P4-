class Node:
    def __init__(self, data, nextNode):
        self._data = data
        self._next = nextNode

LinkedList = [Node(1,1), Node(5,4), Node(7, -1), Node(2, 2), Node(0, 6), Node(8, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
start_pointer = 0
emptylist = 5

def addNode(current_pointer):
    global LinkedList
    global emptylist
    data = int(input('Enter the data: '))

    #check if array is full or not
    if emptylist < 0 or emptylist > 9:
        return False
    else:
        freelist = emptylist
        emptylist = LinkedList[emptylist]._next
        
        #create a new node
        new_node = Node(data, -1)
        
        #store where the freelist is poiting
        LinkedList[freelist] = new_node

        Previous_pointer = 0

        while current_pointer != -1:
            Previous_pointer = current_pointer
            current_pointer = LinkedList[current_pointer]._next

        LinkedList[Previous_pointer]._next = freelist
        