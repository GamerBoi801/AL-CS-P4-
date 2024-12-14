Public Class CircularQueue
    Private Queue() As String
    Private headPointer As Integer
    Private tailPointer As Integer
    Private numberOfItems As Integer

    ' constructor to initialize the circular queue with a specified size
    Public Sub New(size As Integer)
        ReDim Queue(size - 1) ' create an array to hold the queue elements
        headPointer = 0       ' initialize head pointer
        tailPointer = 0       ' initialize tail pointer
        numberOfItems = 0     ' initialize item count
    End Sub

    ' method to enqueue an item into the circular queue
    Public Function Enqueue(item As String) As Boolean
        ' check if the queue is full
        If numberOfItems >= Queue.Length Then
            Console.WriteLine("Queue is full, cannot enqueue.")
            Return False ' return false if the queue is full
        End If

        ' add item to the queue at tailPointer position
        Queue(tailPointer) = item

        ' update tail pointer
        If tailPointer = Queue.Length - 1 Then ' check if at end of queue
            tailPointer = 0 ' wrap around to beginning
        Else 
            tailPointer += 1 ' move to next index 
        End If

        ' increment number of items in the queue 
        numberOfItems += 1 
        Return True ' return true indicating successful enqueue 
    End Function

    ' method to dequeue an item from the circular queue
    Public Function Dequeue() As String
        ' check if the queue is empty
        If numberOfItems = 0 Then
            Console.WriteLine("Queue is empty, cannot dequeue.")
            Return Nothing ' return nothing if the queue is empty
        End If

        ' retrieve item at headPointer position
        Dim item As String = Queue(headPointer)

        ' clear position in the queue (optional)
        Queue(headPointer) = ""

        ' update head pointer
        If headPointer = Queue.Length - 1 Then ' check if at end of queue
            headPointer = 0 ' wrap around to beginning
        Else 
            headPointer += 1 ' move to next index 
        End If

        ' decrement number of items in the queue 
        numberOfItems -= 1 
        Return item ' return the dequeued item 
    End Function

    Public Shared Sub Main()
        Dim cq As New CircularQueue(10) ' create a circular queue of size 10 
        cq.Enqueue("item1")              ' adds 'item1' to the queue 
        cq.Enqueue("item2")              ' adds 'item2' to the queue 

        Dim dequeuedItem As String = cq.Dequeue() ' removes and returns the item at the front of the queue 
        Console.WriteLine("Dequeued: " & dequeuedItem) 

        ' print the current state of the queue (for demonstration)
        Console.WriteLine(String.Join(", ", cq.Queue)) 
    End Sub 
End Class 