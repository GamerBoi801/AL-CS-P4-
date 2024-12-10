## Enqueue in Circular Queue
## Overview

The **enqueue** operation adds an item to the end of a circular queue. A circular queue allows for efficient use of space by connecting the end of the queue back to the beginning, which helps in utilizing available space effectively.

### Components

- **Queue**: An array that holds the elements of the queue.
- **Tail Pointer**: Points to the next position where an element will be enqueued.
- **Number of Items**: Keeps track of how many items are currently in the queue.

## Enqueue Operation Steps

1. **Check if Full**: Before adding an item, check if the queue is full by comparing `number_of_items` with the length of the queue.
   - If the queue is full, print a message and return `False`.

2. **Add Item**: Place the item at the position indicated by `tail_pointer`.

3. **Update Tail Pointer**: Move `tail_pointer` to the next position:
   - If it reaches the end of the array, wrap it around to `0`.
   - Otherwise, simply increment it by 1.

4. **Increment Count**: Increase `number_of_items` by 1 to reflect that an item has been added.

### Python Implementation

Here’s how you can implement the function in Python:

```python
head_pointer = 0
tail_pointer = 0
number_of_items = 0
Queue = [""] * 10  # Initialize  with empty strings

def enqueue(item):
    global head_pointer, tail_pointer, number_of_items

    # Check if the queue is full
    if number_of_items >= len(Queue):
        print("Queue is full, cannot enqueue.")
        return False
    
    # Add item to the queue at tail_pointer position
    Queue[tail_pointer] = item
    
    # Update tail pointer
    if tail_pointer == len(Queue) - 1:  # Check if at end of queue
        tail_pointer = 0  # Wrap around to beginning
    else:
        tail_pointer += 1  # Move to next index
    
    # Increment number of items in the queue
    number_of_items += 1
    return True

# Example usage
enqueue('item1')  # Adds 'item1' to the queue
enqueue('item2')  # Adds 'item2' to the queue
print(Queue)      # Output: ['item1', 'item2', '', '', '', '', '', '', '', '']

```
## Java Implementation

Here’s how you can implement the `enqueue` operation in Java:

```java
public class CircularQueue {
    private String[] queue;
    private int headPointer;
    private int tailPointer;
    private int numberOfItems;

    // Constructor to initialize the queue with a specified size
    public CircularQueue(int size) {
        queue = new String[size];  // Create an array to hold the queue elements
        headPointer = 0;            // Initialize head pointer
        tailPointer = 0;            // Initialize tail pointer
        numberOfItems = 0;         // Initialize item count
    }

    // Method to enqueue an item into the circular queue
    public boolean enqueue(String item) {
        // Check if the queue is full
        if (numberOfItems >= queue.length) {
            System.out.println("Queue is full, cannot enqueue.");
            return false;  // Return false if the queue is full
        }

        // Add item to the queue at tailPointer position
        queue[tailPointer] = item;

        // Update tail pointer
        if (tailPointer == queue.length - 1) {  // Check if at end of queue
            tailPointer = 0;  // Wrap around to beginning
        } else {
            tailPointer++;  // Move to next index
        }

        // Increment number of items in the queue
        numberOfItems++;
        return true;  // Return true indicating successful enqueue
    }

    public static void main(String[] args) {
        CircularQueue cq = new CircularQueue(10);  // Create a circular queue of size 10
        cq.enqueue("item1");  // Adds 'item1' to the queue
        cq.enqueue("item2");  // Adds 'item2' to the queue
        
        // Print the current state of the queue (for demonstration)
        System.out.println(java.util.Arrays.toString(cq.queue));  
    }
}
```
## Visual Basic Implementation

Here’s how you can implement the `enqueue` operation in Visual Basic:

```vb
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

    Public Shared Sub Main()
        Dim cq As New CircularQueue(10) ' create a circular queue of size 10 
        cq.Enqueue("item1")              ' adds 'item1' to the queue 
        cq.Enqueue("item2")              ' adds 'item2' to the queue 

        ' print the current state of the queue (for demonstration)
        Console.WriteLine(String.Join(", ", cq.Queue)) 
    End Sub 
End Class 
```

## Pseudocode Implementation

Here’s how you can implement the `enqueue` operation in **Psuedocode**:
```
// define the circular queue structure
DECLARE Queue AS ARRAY OF STRING

DECLARE headPointer AS INTEGER

DECLARE tailPointer AS INTEGER

DECLARE numberOfItems AS INTEGER


// constructor to initialize the circular queue with a specified size
PROCEDURE InitializeQueue(size: INTEGER)

    SET Queue = NEW ARRAY OF STRING[size]

    SET headPointer = 0

    SET tailPointer = 0

    SET numberOfItems = 0

ENDPROCEDURE


// method to enqueue an item into the circular queue
FUNCTION Enqueue(item: STRING) RETURNS BOOLEAN

    // check if the queue is full
    IF numberOfItems >= LENGTH(Queue) THEN

        PRINT "Queue is full, cannot enqueue."

        RETURN FALSE // return false if the queue is full

    ENDIF


    // add item to the queue at tailPointer position
    Queue[tailPointer] = item


    // update tail pointer
    IF tailPointer = LENGTH(Queue) - 1 THEN // check if at end of queue

        SET tailPointer = 0 // wrap around to beginning

    ELSE 

        SET tailPointer = tailPointer + 1 // move to next index 

    ENDIF


    // increment number of items in the queue 
    SET numberOfItems = numberOfItems + 1 

    RETURN TRUE // return true indicating successful enqueue 

ENDFUNCTION


// main program to demonstrate usage of circular queue
BEGIN

    DECLARE cq AS CircularQueue

    CALL InitializeQueue(10) // create a circular queue of size 10 

    CALL Enqueue("item1")     // adds 'item1' to the queue 

    CALL Enqueue("item2")     // adds 'item2' to the queue 


    // print the current state of the queue (for demonstration)
    FOR i FROM 0 TO LENGTH(Queue) - 1 DO

        PRINT Queue[i]

    NEXT i

END
```