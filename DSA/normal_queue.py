# Global variables for managing the circular queue
head_pointer = 0
tail_pointer = 0
number_of_items = 0
Queue = [""] * 10  # Initialize a fixed-size queue with empty strings

def enqueue(item):
    global head_pointer, tail_pointer, number_of_items  # Declare globals to modify them

    # Check if the queue is full
    if number_of_items >= len(Queue):  
        print("Queue is full, cannot enqueue.")
        return False
    
    # Add item to the queue at tail_pointer position
    Queue[tail_pointer] = item
    
    # moving the tail ptr
    if tail_pointer == len(Queue) - 1: #checking if it is at the end of the queue
        tail_pointer = 0
    else:
        tail_pointer += 1
    
    
    # Increment the number of items in the queue
    number_of_items += 1
    return True

# Example usage
enqueue('lol')
print(Queue) 

def dequeue():
    global head_pointer, tail_pointer, number_of_items
    if number_of_items == 0:
        print('Queue is empty')
        return False
    
    item = Queue[head_pointer]  # Retrieve the item at head_pointer
    Queue[head_pointer] = ""    # Set the position to an empty string (or None)
    
    # Move head_pointer circularly
    head_pointer += 1
    if head_pointer == len(Queue):  # Check if we've reached the end
        head_pointer = 0  # Wrap around to the beginning
    
    number_of_items -= 1  # Decrement the count of items in the queue

    return item  # Return the dequeued item

# Example usage
dequeue()  # Attempt to dequeue from an empty queue (if Queue is initially empty)
print(Queue)  # Print the current state of the queue