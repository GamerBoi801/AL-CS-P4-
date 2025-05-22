null = None
class Node:
    def __init__(self, data):
        self.data = data
        self.left = null  
        self.right = null  

root_ptr = null    

def add(data): 
    global root_ptr
    
    # checks if the tree is empty; if root_ptr is null 
    if root_ptr is null:
        root_ptr = Node(data)
        print(f'added root node: {data}')
        return
    
    #  keeping track of the current node 
    current = root_ptr

    while True:  
        if data < current.data:
            if current.left is null:  
                current.left = Node(data)
                print(f'Added node {data} to the left of {current.data}')
                break  # exits the loop after insertion
            else:
                current = current.left

        elif data > current.data:
            if current.right is null:  #checks if right child is null
                current.right = Node(data)
                print(f'Added node {data} to the right of {current.data}')
                break  #exist the loop after insertion
        
        else: #if the nodes are equal then doesn't add them  
            print(f'node {data} already exists.')
            return

#test case for addition
add(10)
add(5)
add(15)
add(10)  # checking the equal scenario

def search(data):
    global root_ptr
    
    # check if the tree is empty
    if root_ptr is None:  # use None instead of null
        print('tree is empty')
        return
    
    current = root_ptr  # start at the root node

    while current is not None:  # continue until we reach a leaf node
        if current.data == data:  # check if we found the target value
            print(f'found {data} in the tree')
            return
        
        # decide which direction to go based on comparison
        if data < current.data:  # target is less than current node's data
            current = current.left  # move to the left child
        else:  # target is greater than current node's data
            current = current.right  # move to the right child

    # exiting the loop,  meaning we did not find the value
    print(f'{data} not found in binary tree.')

search(10)
search(15)

#print the tree
def print_tree():
    global root_ptr
    
    current = root_ptr
    
    if current.left == None:
        print(current.right)
        print_tree(current.right)
    elif current.right == None:
        print(current.left)
        print_tree(current.left)
