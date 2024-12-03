# Enqueue Operation in Circular Queue

This document provides an overview of the `enqueue` operation in a circular queue implementation in Python.

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

### Example Code Snippet

Here’s a code snippet demonstrating the `enqueue` operation:

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

## Dequeue

The **dequeue** operation removes an item from the front of a circular queue. A circular queue allows for efficient use of space by connecting the end of the queue back to the beginning, which helps in utilizing available space effectively.

### Key Components

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

### Example Code Snippet

Here’s a code snippet demonstrating the `dequeue` operation:

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