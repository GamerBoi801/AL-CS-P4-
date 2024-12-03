# Initialize an empty stack
stack = [None] * 10  # Create a fixed-size stack with a limit of 10 elements

# Initialize pointers for the stack
topPointer = -1  # Set to -1 to indicate that the stack is empty
basePointer = 0  # Base pointer for the stack (not used in this implementation)
limit = 10       # Maximum size of the stack

def push(item):
    global topPointer  # Declare topPointer as global to modify it
    if topPointer < limit - 1:  # Check if there is space in the stack
        topPointer += 1  # Move the top pointer up
        stack[topPointer] = item  # Add the item to the stack at the new top position
    else:
        print("Stack is full")  # Print message if the stack is full

def pop():
    global topPointer  # Declare topPointer as global to modify it
    if topPointer == -1:  # Check if the stack is empty
        print('Stack is empty, cannot pop')  # Print message if the stack is empty
        return None  # Return None to indicate no item was popped
    else:
        item = stack[topPointer]  # Get the item at the current top position
        topPointer -= 1  # Move the top pointer down to remove the item
        return item  # Return the popped item

# Example usage:
push(5)         # Push an item onto the stack
push(10)        # Push another item onto the stack
print(pop())    # Pop an item from the stack (should return 10)
print(pop())    # Pop another item from the stack (should return 5)
print(pop())    # Attempt to pop from an empty stack (should print message)