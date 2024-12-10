## Dequeue

The **dequeue** operation removes an item from the front of a circular queue. A circular queue allows for efficient use of space by connecting the end of the queue back to the beginning, which helps in utilizing available space effectively.

###  Components

- **Queue**: An array that holds the elements of the queue.
- **Head Pointer**: Points to the front of the queue (the position from which elements are dequeued).
- **Number of Items**: Keeps track of how many items are currently in the queue.

## Dequeue Operation Steps

1. **Check if Empty**: Before removing an item, check if the queue is empty by verifying if `number_of_items` is `0`.
   - If the queue is empty, print a message and return `False`.

2. **Retrieve Item**: Get the item at the position indicated by `head_pointer`.

3. **Clear Position**: Optionally set that position in the queue to an empty value (like an empty string) to indicate it is now free.

4. **Update Head Pointer**: Move `head_pointer` to the next position:
   - If it reaches the end of the array, wrap it around to `0`.
   
5. **Decrement Count**: Decrease `number_of_items` by 1 to reflect that an item has been removed.

### Python Implementation


```python
# Global variables for managing the circular queue
head_pointer = 0
tail_pointer = 0
number_of_items = 0
Queue = [""] * 10  # Initialize a fixed-size queue with empty strings

def dequeue():
    global head_pointer, tail_pointer, number_of_items
    
    # Check if the queue is empty
    if number_of_items == 0:
        print('Queue is empty')
        return False
    
    # Retrieve item at head_pointer
    item = Queue[head_pointer]
    
    # Clear position in the queue
    Queue[head_pointer] = ""
    
    # Update head pointer
    head_pointer += 1
    if head_pointer == len(Queue):  # Check if we've reached the end
        head_pointer = 0  # Wrap around to beginning
    
    # Decrement number of items in the queue
    number_of_items -= 1  
    return item  # Return the dequeued item

# Example usage
dequeued_item = dequeue()  # Removes and returns the item at the front of the queue
print(dequeued_item)       # Output: The item that was dequeued (or None if empty)
```

### Java Implementaton
```java 
public class CircularQueue {
    private String[] queue;
    private int headPointer;
    private int tailPointer;
    private int numberOfItems;

    // Constructor to initialize the circular queue with a specified size
    public CircularQueue(int size) {
        queue = new String[size]; // create an array to hold the queue elements
        headPointer = 0;          // initialize head pointer
        tailPointer = 0;          // initialize tail pointer
        numberOfItems = 0;        // initialize item count
    }

    // Method to enqueue an item into the circular queue
    public boolean enqueue(String item) {
        // check if the queue is full
        if (numberOfItems >= queue.length) {
            System.out.println("Queue is full, cannot enqueue.");
            return false; // return false if the queue is full
        }

        // add item to the queue at tailPointer position
        queue[tailPointer] = item;

        // update tail pointer
        if (tailPointer == queue.length - 1) { // check if at end of queue
            tailPointer = 0; // wrap around to beginning
        } else {
            tailPointer++; // move to next index 
        }

        // increment number of items in the queue 
        numberOfItems++; 
        return true; // return true indicating successful enqueue 
    }

    // Method to dequeue an item from the circular queue
    public String dequeue() {
        // check if the queue is empty
        if (numberOfItems == 0) {
            System.out.println("Queue is empty, cannot dequeue.");
            return null; // return null if the queue is empty
        }

        // retrieve item at headPointer position
        String item = queue[headPointer];

        // clear position in the queue (optional)
        queue[headPointer] = null;

        // update head pointer
        if (headPointer == queue.length - 1) { // check if at end of queue
            headPointer = 0; // wrap around to beginning
        } else {
            headPointer++; // move to next index 
        }

        // decrement number of items in the queue 
        numberOfItems--; 
        return item; // return the dequeued item 
    }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(10); // create a circular queue of size 10 
        cq.enqueue("item1");                       // adds 'item1' to the queue 
        cq.enqueue("item2");                       // adds 'item2' to the queue 

        String dequeuedItem = cq.dequeue();       // removes and returns the item at the front of the queue 
        System.out.println("Dequeued: " + dequeuedItem); 

        // print the current state of the queue (for demonstration)
        for (String item : cq.queue) {
            System.out.print(item + " ");
        }
    }
}
```
## Visual Basic Implementation
``` VB
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
```
## Psuedocode 
```
// Define the circular queue structure
DECLARE Queue AS ARRAY OF STRING
DECLARE headPointer AS INTEGER
DECLARE tailPointer AS INTEGER
DECLARE numberOfItems AS INTEGER

// Constructor to initialize the circular queue with a specified size
PROCEDURE InitializeQueue(size: INTEGER)
    SET Queue = NEW ARRAY OF STRING[size]
    SET headPointer = 0
    SET tailPointer = 0
    SET numberOfItems = 0
ENDPROCEDURE

// Method to enqueue an item into the circular queue
FUNCTION Enqueue(item: STRING) RETURNS BOOLEAN
    // Check if the queue is full
    IF numberOfItems >= LENGTH(Queue) THEN
        PRINT "Queue is full, cannot enqueue."
        RETURN FALSE // Return false if the queue is full
    ENDIF

    // Add item to the queue at tailPointer position
    Queue[tailPointer] = item

    // Update tail pointer
    IF tailPointer = LENGTH(Queue) - 1 THEN // Check if at end of queue
        SET tailPointer = 0 // Wrap around to beginning
    ELSE 
        SET tailPointer = tailPointer + 1 // Move to next index 
    ENDIF

    // Increment number of items in the queue 
    SET numberOfItems = numberOfItems + 1 
    RETURN TRUE // Return true indicating successful enqueue 
END FUNCTION

// Method to dequeue an item from the circular queue
FUNCTION Dequeue() RETURNS STRING
    // Check if the queue is empty
    IF numberOfItems = 0 THEN
        PRINT "Queue is empty, cannot dequeue."
        RETURN NULL // Return null if the queue is empty
    ENDIF

    // Retrieve item at headPointer position
    DECLARE item AS STRING = Queue[headPointer]

    // Clear position in the queue (optional)
    Queue[headPointer] = ""

    // Update head pointer
    IF headPointer = LENGTH(Queue) - 1 THEN // Check if at end of queue
        SET headPointer = 0 // Wrap around to beginning
    ELSE 
        SET headPointer = headPointer + 1 // Move to next index 
    ENDIF

    // Decrement number of items in the queue 
    SET numberOfItems = numberOfItems - 1 
    RETURN item // Return the dequeued item 
END FUNCTION

// Main program for demonstration purposes 
BEGIN 
    DECLARE cq AS CircularQueue 
    CALL InitializeQueue(10) // Create a circular queue of size 10 

    CALL Enqueue("item1")     // Adds 'item1' to the queue 
    CALL Enqueue("item2")     // Adds 'item2' to the queue 

    DECLARE dequeuedItem AS STRING 
    SET dequeuedItem = Dequeue() // Removes and returns an item from the front of the queue 

    PRINT "Dequeued: " + dequeuedItem 

END 
```
